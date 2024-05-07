cases = int(input())

for _ in range(cases):
    n = int(input())
    arr = []
    for _ in range(n):
        name, amount = input().split()
        amount = int(amount)
        arr.append((name, amount))
    arr = sorted(arr, key=lambda x: x[1], reverse=True)
    print(arr[0][0])
