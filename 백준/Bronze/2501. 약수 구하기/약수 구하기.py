n, k = map(int, input().split())

divisor = [i for i in range(1, n+1) if n % i == 0]

if len(divisor) < k:
    print(0)
else:
    print(divisor[k-1])
