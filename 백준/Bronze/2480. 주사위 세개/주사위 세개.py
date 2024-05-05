dices = list(map(int, input().split()))

dices.sort(reverse=True)

num = [dice for dice in dices if dices.count(dice) > 1]

if len(num) == 3:
    print(10000 + num[0] * 1000)
elif len(num) == 2:
    print(1000 + num[0] * 100)
else:
    print(dices[0] * 100)

