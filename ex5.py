class Book:
    def __init__(self, title, quantity):
        self.title = title
        self.quantity = quantity


c = input("Enter the quantity of books: ")
while c.isdigit() == False or int(c) <= 0:
    c = input(
        "Quantity must be a number and be greater than zero. Enter quantity try again : ")
c = int(c)
books = []
for i in range(1, c+1):
    name = input("Enter your title's book {}: ".format(i))
    quantity = input("Enter quantity of {}: ".format(name))
    while quantity.isdigit() == False or int(quantity) <= 0:
        quantity = input(
            "Quantity must be a number and be greater than zero. Enter quantity try again : ")
    books.append(Book(name, quantity))
key = input("Enter your key :")
count = len(list(filter(lambda book: book.title == key, books)))
if count > 0:
    print("{} avaiable".format(count))
else:
    print("Out of stock")
