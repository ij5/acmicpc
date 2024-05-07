dishes = list(input())

height = 0

cache = ''
for i, dish in enumerate(dishes):
    if dish == cache:
        height += 5
    elif dish != cache:
        height += 10
    cache = dish

print(height)