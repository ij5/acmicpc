nums = list(map(int, input().split()))

verifier = sum([n**2 for n in nums]) % 10

print(verifier)