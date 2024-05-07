dots = int(input())

coords = [0] * 5

for dot in range(dots):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        coords[0] += 1
    elif x > 0 and y > 0:
        coords[1] += 1
    elif x < 0 and y > 0:
        coords[2] += 1
    elif x < 0 and y < 0:
        coords[3] += 1
    elif x > 0 and y < 0:
        coords[4] += 1

print(f"Q1: {coords[1]}\nQ2: {coords[2]}\nQ3: {coords[3]}\nQ4: {coords[4]}\nAXIS: {coords[0]}")
