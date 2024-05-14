n = int(input())

print('\n'.join([('*' * i).center(n*2)[:-n+j-1] for i, j in zip(range(1, n*2, 2), range(1, n+1))]))
