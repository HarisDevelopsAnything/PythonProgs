import pickle
import random

class Book:
    FILENAME = "books.bin"

    def __init__(self, id, name, author, pub, price):
        self.id = id
        self.name = name
        self.author = author
        self.pub = pub
        self.price = price

    def addBook(self):
        with open(Book.FILENAME, "ab") as lib:
            pickle.dump(self, lib)
        print(f"Book {self.name} added to the library.")

    def removeBook(id):
        books = []
        with open(Book.FILENAME, "rb") as lib:
            try:
                while True:
                    book = pickle.load(lib)
                    if book.id != id:
                        books.append(book)
            except EOFError:
                pass

        with open(Book.FILENAME, "wb") as lib:
            for i in books:
                pickle.dump(i, lib)

    @staticmethod
    def showBooks():
        with open(Book.FILENAME, "rb") as lib:
            try:
                while True:
                    book = pickle.load(lib)
                    print(f"Name: {book.name}")
                    print(f"Author: {book.author}")
                    print(f"Publisher: {book.pub}")
                    print(f"Price: {book.price}")
            except EOFError:
                print("Completed.")

while True:
    print("1) Add book\n2) Remove book\n3) Show books\n4) Exit")
    try:
        ch = int(input("Your choice: ")[0])
    except ValueError:
        print("Invalid choice! Please enter a number.")
        continue

    if ch == 1:
        id = str(random.randint(1000, 9999))
        print(f"Book ID: {id}")
        name = input("Book name: ")
        author = input("Author name: ")
        pub = input("Publisher: ")
        price = input("Price: ")
        book = Book(id, name, author, pub, price)
        book.addBook()
    elif ch == 2:
        Book.showBooks()
        id = input("Enter the ID of the book to remove: ")
        Book().removeBook(id)
    elif ch == 3:
        Book.showBooks()
    elif ch == 4:
        print("Exiting.")
        break
    else:
        print("Invalid choice! Please choose a number between 1 and 4.")
