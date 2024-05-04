score = int(input())

score_map = dict(    
    A = range(90, 101),
    B = range(80, 90),
    C = range(70, 80),
    D = range(60, 70),
    F = range(0, 60)
)

for k, v in score_map.items():
    if score in v:
        print(k)
        break
