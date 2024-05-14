semester = int(input())

for _ in range(semester):
    subjects = int(input())
    credit = 0
    grades = []
    for _ in range(subjects):
        c, g = map(float, input().split())
        credit += int(c)
        grades.append(g * c)
    print(credit, sum(grades) / credit)
