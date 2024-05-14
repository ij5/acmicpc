num_school = int(input())

remain = 0

for _ in range(num_school):
    students, apples = map(int, input().split())
    remain += apples % students

print(remain)