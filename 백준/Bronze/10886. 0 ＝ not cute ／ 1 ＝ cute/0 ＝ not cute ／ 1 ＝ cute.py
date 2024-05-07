persons = int(input())

arr = []

for _ in range(persons):
    arr.append(int(input()))

print("Junhee is not cute!" if arr.count(0) > arr.count(1) else "Junhee is cute!")