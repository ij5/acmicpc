n, x = map(int, input().split())

arr = list(map(int, input().split()))

print(' '.join([str(i) for i in arr if i < x]))
