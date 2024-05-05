scores = 0

for _ in range(5):
    score = int(input())
    scores += score if score >= 40 else 40

print(scores // 5)