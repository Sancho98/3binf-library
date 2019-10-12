class Book:
    def __init__(self, title, author, sbn):
    self.title = title
    self.author = author
    self.sbn = sbn


harry_potter = Book("Harry Potter e il calice di fuoco",
                    "J.K Rowling")
print(harry_potter.title)
print(harry_potter.author)
print(harry_potter.sbn)
