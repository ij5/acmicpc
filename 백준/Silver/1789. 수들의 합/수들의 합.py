S = int(input())

total = 0
count = 0

for i in range(1, S + 1):
    if total + i > S:
        break
    total += i
    count += 1

print(count)