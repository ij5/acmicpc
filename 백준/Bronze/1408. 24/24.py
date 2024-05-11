from datetime import date, time, timedelta, datetime

current = datetime.combine(date.min, time(*map(int, input().split(":"))))
t = input()
if t == "":
    started = current
else:
    started = datetime.combine(date.min, time(*map(int, t.split(":"))))

day1 = timedelta(days=1)

remain = started + day1
remain = remain - current

print(f"{(datetime.min + remain).time()}")
