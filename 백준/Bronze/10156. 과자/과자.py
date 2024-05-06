price, amount, remain = map(int, input().split())

total = price * amount
print(total - remain if total >= remain else 0)