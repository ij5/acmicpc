game = {
    (1, 3): 'A',
    (2, 2): 'B',
    (3, 1): 'C',
    (4, 0): 'D',
    (0, 4): 'E'
}

for _ in range(3):
    binary = list(map(int, input().split()))
    zero = binary.count(0)
    one = binary.count(1)
    print(game[(zero, one)])
