cases = int(input())

for _ in range(cases):
    car_price = int(input())
    n = int(input())
    for _ in range(n):
        opt_count, opt_price = map(int, input().split())
        car_price += opt_count * opt_price
    print(car_price)
