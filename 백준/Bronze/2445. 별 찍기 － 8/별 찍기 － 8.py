n = int(input())

for i in range(n*2-2, 0, -2):
    print((' ' * i).center(n*2, '*'))

for i in range(0, n*2, 2):
    print((' ' * i).center(n*2, '*'))