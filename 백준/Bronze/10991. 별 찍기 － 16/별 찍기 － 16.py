n = int(input())

for i in range(1, n+1):
    star = ("* " * i).center(n*2 - 1)
    print(star.rstrip())
