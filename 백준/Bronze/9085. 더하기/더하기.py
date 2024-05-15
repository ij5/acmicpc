cases = int(input())

for _ in range(cases):
    n = int(input())
    print(sum([x for x in list(map(int, input().split()))]))