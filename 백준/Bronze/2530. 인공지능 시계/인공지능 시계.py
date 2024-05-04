h, m, s = map(int, input().split())
add = int(input())

s += add % 60
m += add // 60

if s >= 60:
    m += s // 60
    s %= 60

if m >= 60:
    h += m // 60
    m %= 60

h %= 24

print(h, m, s)
