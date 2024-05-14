n = int(input())

print('\n'.join([('*' * i).center(n*2)[:-j] for i, j in zip(range(n*2-1, 0, -2), range(1, n+1))]))
