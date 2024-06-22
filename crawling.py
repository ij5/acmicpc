from playwright.async_api import async_playwright
from tqdm.auto import tqdm
import pandas as pd
import re
from datetime import datetime
import asyncio
import os
import sys

url = r"https://search.naver.com/search.naver?sm=tab_hty.top&ssc=tab.blog.all&query=openai&oquery=openai&tqi=iC0Gllqo1awssMEfLCZssssstnV-489802&nso=so%3Ar%2Cp%3Afrom20240401to20240430"

df = pd.DataFrame()
skip = False
if os.path.exists('dataset.csv'):
    df = pd.read_csv('dataset.csv')
    skip = True # 만약 데이터셋 파일이 있으면 마지막으로 가져온 데이터까지 스킵

TOTAL_DATASET = 1000

num_dataset = TOTAL_DATASET

async def main():
    global num_dataset, skip, df # 글로벌 변수 선언
    print('crawling started...')
    dataset = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False) # headless=False 를 사용하여 브라우저 화면 모니터링
        context = await browser.new_context() # 새로운 context 생성
        page = await context.new_page() # 새 페이지 열기
        await page.goto(url)
        i = 0
        progress = tqdm(total=num_dataset) # tqdm 라이브러리를 사용하여 현재 진행 상황 출력
        while True:
            if i >= num_dataset or progress.n >= TOTAL_DATASET: # TOTAL_DATASET보다 tqdm 진행 상황이 크면 반복문 종료
                break
            blog_list = page.locator(".lst_view>*") # HTML lst_view 클래스의 모든 하위 태그 가져오기
            blog = blog_list.nth(i) # .nth(n) 함수로 네이버 검색 결과 중 하나 가져오기
            if not await blog.is_visible(): # 검색 결과 중간에 보이지 않는 태그가 끼어있으므로 무시하고 계속 진행
                i += 1
                num_dataset += 1
                continue
            if i + 10 >= await blog_list.count(): # 검색 결과 수가 i+1보다 작아지면 맨 밑으로 스크롤하여 다음 결과 로딩
                try:
                    await page.locator('#footer').scroll_into_view_if_needed()
                except Exception as e:
                    print(e)
                    break
            # await blog.scroll_into_view_if_needed()
            if skip and df.index.stop > progress.n: # 데이터셋 파일이 존재하고 
                i += 1
                num_dataset += 1
                progress.update(1)
                continue
            else:
                skip = False
            blog_info = blog.locator(".title_link")
            blog_title = await blog_info.text_content()
            blog_url = await blog_info.get_attribute('href')
            article = await context.new_page()
            try:
                await article.goto(blog_url)
            except Exception:
                i += 1
                num_dataset += 1
                continue
            if 'm.blog.naver.com' in blog_url:
                content = article.locator('.se-main-container')
                time = await article.locator('.blog_date').text_content()
                if time is not None:
                    time = datetime.strptime(time, '%Y. %m. %d. %H:%M')
            elif 'blog.naver.com' in blog_url:
                iframe = article.frame_locator('#mainFrame')
                content = iframe.locator('.se-main-container')
                time = await iframe.locator('.se_publishDate').text_content()
                if time is not None:
                    time = datetime.strptime(time, '%Y. %m. %d. %H:%M')
            elif 'tistory.com' in blog_url:
                content = await article.query_selector('.contents_style')
                if content is None:
                    content = await article.query_selector('#article')
                if content is None:
                    i += 1
                    num_dataset += 1
                    continue
                time = await article.locator('[property="og:regDate"]').get_attribute('content')
                if time is not None:
                    time = datetime(int(time[0:4]), int(time[4:6]), int(time[6:8]), int(time[8:10]), int(time[10:12]), int(time[12:14])) # ex) 20200807105932
            else:
                i += 1
                num_dataset += 1
                await article.close()
                continue
            try:
                text_content = await content.text_content(timeout=3000)
            except Exception as e:
                i += 1
                num_dataset += 1
                await article.close()
                continue
            
            dataset.append(dict(
                title=blog_title,
                url=blog_url,
                content=re.sub(r'\s+', ' ', text_content),
                time=time,
            ))
            await article.close()

            progress.update(1)
            i += 1
            if (i + 1) % 100 == 0:
                df = pd.concat([df, pd.DataFrame(dataset)], ignore_index=True)
                dataset = []
                df.to_csv('dataset.csv')
    
    sys.stdout.flush()
    df = pd.concat([df, pd.DataFrame(dataset)], ignore_index=True)
    df.to_csv('dataset.csv')


asyncio.run(main())
