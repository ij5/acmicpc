n = int(input())

for i in range(n*2-1, 1, -2):
    print(("*" * i).center(n*2-1).rstrip())

for i in range(1, n*2, 2):
    print(("*" * i).center(n*2-1).rstrip())