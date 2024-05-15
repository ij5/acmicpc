import math

m = int(input())
n = int(input())

primes = []

for i in range(m, n+1):
    if i <= 1:
        continue
    prime = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            prime = False
            break
    if prime: primes.append(i)

if len(primes) >= 1:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)
