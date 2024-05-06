from collections import Counter

xarr = []
yarr = []

for _ in range(3):
    x, y = map(int, input().split())
    xarr.append(x)
    yarr.append(y)

xc = Counter(xarr)
xarr = sorted(xarr, key=xc.get)

yc = Counter(yarr)
yarr = sorted(yarr, key=yc.get)

print(xarr[0], yarr[0])