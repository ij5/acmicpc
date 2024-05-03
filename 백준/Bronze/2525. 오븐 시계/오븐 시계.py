hour, minute = map(int, input().split())
timer = int(input())

h = hour + timer // 60
m = minute + timer % 60
if m >= 60:
    h += 1
    m %= 60

if h >= 24:
    h %= 24

print(h, m)