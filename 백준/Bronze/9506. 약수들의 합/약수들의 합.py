while True:
    n = int(input())
    if n == -1:
        break
    arr = []
    for i in range(1, int(n ** (1/2)) + 1):
        if n % i == 0:
            arr.append(i)
            if (i ** 2) != n:
                arr.append(n // i)
    arr.sort()
    arr = arr[:-1]
    if sum(arr) == n:
        print(f"{n} = {' + '.join([str(x) for x in arr])}")
    else:
        print(f"{n} is NOT perfect.")
