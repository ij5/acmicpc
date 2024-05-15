passengers = 0
peak = []

for _ in range(4):
    leave, enter = map(int, input().split())
    passengers -= leave
    passengers += enter
    peak.append(passengers)

print(max(peak))