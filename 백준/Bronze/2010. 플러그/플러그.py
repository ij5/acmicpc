import sys

input = sys.stdin.readline

n = int(input())

total = 0

for i in range(n):
    count = int(input())
    if i + 1 == n:
        total += count
    else:
        total += count - 1

print(total)
