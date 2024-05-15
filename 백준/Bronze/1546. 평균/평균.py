count = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
average = sum(map(lambda x: x / max_score * 100, scores)) / count
print(average)