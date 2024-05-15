cases = int(input())

for _ in range(cases):
    v, e = map(int, input().split())
    print(e - v + 2)
