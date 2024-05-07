count = int(input())

persons = []

for _ in range(count):
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    num = [x for x in arr if arr.count(x) > 1]
    l = len(num)
    if l == 3:
        persons.append(10000 + num[0] * 1000)
    elif l == 2:
        persons.append(1000 + num[0] * 100)
    else:
        persons.append(arr[0] * 100)

persons.sort(reverse=True)
print(persons[0])