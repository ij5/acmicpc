cases = int(input())

queue = []

for _ in range(cases):
    plain, adv, cost = map(int, input().split())
    if plain == adv - cost:
        queue.append("does not matter")
    elif plain < adv - cost:
        queue.append("advertise")
    elif plain > adv - cost:
        queue.append("do not advertise")

print('\n'.join(queue))
