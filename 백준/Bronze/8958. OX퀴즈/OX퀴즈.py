cases = int(input())

for _ in range(cases):
    scores = list(input())
    i = 0
    total = 0
    for score in scores:
        if score == 'O':
            i += 1
            total += i
        elif score == 'X':
            i = 0
    print(total)
