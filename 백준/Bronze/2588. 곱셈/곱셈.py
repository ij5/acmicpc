a = int(input())
b = list(map(int, list(input())))

inc = 1
indent = 0
total = 0

for i in range(2, -1, -1):
    mul = b[i] * a * inc
    inc *= 10
    total += mul
    print(str(mul)[:-indent if indent != 0 else 4])
    indent += 1

print(total)
