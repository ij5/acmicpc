count = int(input())

cases = []

for i in range(count):
    a, b = map(int, input().split())
    cases.append(a + b)

for i, case in enumerate(cases):
    print(f"Case #{i+1}: {case}")
