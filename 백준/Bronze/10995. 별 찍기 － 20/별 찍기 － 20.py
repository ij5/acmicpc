n = int(input())

for i in range(1, n+1):
    if i % 2 == 0:
        star = " *" * n
    else:
        star = "* " * n
    print(star.rstrip())
