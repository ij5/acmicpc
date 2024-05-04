cases = int(input())

result = ""

for _ in range(cases):
    R, S = input().split()
    R = int(R)
    S = list(S)
    result += ''.join(x*R for x in S)
    result += '\n'

print(result.strip())
