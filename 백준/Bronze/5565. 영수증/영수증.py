total_price = int(input())

books = []
for _ in range(9):
    books.append(int(input()))

print(total_price - sum(books))
