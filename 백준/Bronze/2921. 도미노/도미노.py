n = int(input())

dots = [(i, j) for j in range(0, n+1) for i in range(0, n+1)]

unique_dots = list(set(map(lambda x: tuple(sorted(x)), dots)))

print(sum([x + y for x, y in unique_dots]))
