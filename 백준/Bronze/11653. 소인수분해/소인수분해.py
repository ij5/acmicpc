N = int(input())

if N != 1:
    i = 2
    while True:
        if N % i == 0:
            N //= i
            print(i)
        else:
            i += 1
        if N == 1:
            break
