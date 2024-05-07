mirror = input()

start = len(mirror) // 2
reverse = list(mirror[:start])
reverse.reverse()
reverse = ''.join(reverse)

if mirror.endswith(reverse):
    print(1)
else:
    print(0)

