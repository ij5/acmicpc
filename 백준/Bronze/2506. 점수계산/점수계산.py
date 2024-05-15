count = int(input())

result = list(map(int, input().split()))

prev = 0
score = 0

for i in result:
    if i == 1:
        prev += 1
        score += prev
    else:
        prev = 0

print(score)