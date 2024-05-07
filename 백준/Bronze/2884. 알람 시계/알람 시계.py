H, M = map(int, input().split())

sub = M - 45
m = (60 - abs(sub) % 60) if sub < 0 else sub
h = (H - 1) if sub < 0 else H

print(23 if h < 0 else h, m)
