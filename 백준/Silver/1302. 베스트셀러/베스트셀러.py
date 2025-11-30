n = int(input())

books = {}

for _ in range(n):
    name = input().strip()
    books[name] = books.get(name, 0) + 1

sorted_books = sorted(books.items(), key=lambda x: (-x[1], x[0]))
print(sorted_books[0][0])
