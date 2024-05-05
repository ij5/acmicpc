import sys
input = sys.stdin.readline

cases = int(input())

queue = []

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def lcd(a, b):
    return a * b // gcd(a, b)

for _ in range(cases):
    a, b = map(int, input().split())
    print(lcd(a, b))
