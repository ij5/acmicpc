cscore, sscore = 100, 100

round = int(input())

for _ in range(round):
    c, s = map(int, input().split())
    if c < s:
        cscore -= s
    elif c > s:
        sscore -= c

print(cscore)
print(sscore)