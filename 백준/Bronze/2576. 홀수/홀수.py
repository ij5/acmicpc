odds = []

for _ in range(7):
    num = int(input())
    if num % 2 == 1:
        odds.append(num)

if len(odds) == 0:
    print(-1)
else:
    print(sum(odds))
    print(min(odds))
