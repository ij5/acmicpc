queue = []

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    queue.append("Yes" if a > b else "No")

print('\n'.join(queue))