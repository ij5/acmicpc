import math

n = int(input())

x = list(map(int, input().split()))

count = 0

for i in x:
    if i <= 1:
        continue
    prime = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            prime = False
            break
    if prime: count += 1

print(count)
