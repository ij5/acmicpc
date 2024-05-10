import math

m = int(input())
n = int(input())

arr = []

for i in range(m, n+1):
    complete = math.sqrt(i)
    if complete.is_integer():
        arr.append(i)

arr.sort()

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr), arr[0], sep='\n')
