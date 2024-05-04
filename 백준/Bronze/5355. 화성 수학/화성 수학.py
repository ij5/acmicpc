cases = int(input())

queue = []

for c in range(cases):
    op = input().split()
    num = float(op[0])
    for operator in op[1:]:
        if operator == '@':
            num *= 3
        elif operator == '%':
            num += 5
        elif operator == '#':
            num -= 7
    queue.append(num)

for n in queue:
    print(f"{n:.2f}")
