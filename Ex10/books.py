import pickle
import random
class Book:
    def __init__(self, id, name, author, pub, price):
        self.id= id
        self.name= name
        self.author= author
        self.pub= pub
        self.price= price
    def addBook(self):
        lib= open("books.bin", "ab+")
        lib.seek(2)
        pickle.dump(self, lib)
        print(f"Book {self.name} added to the library.")
        lib.close()
    def removeBook(id):
        books = []
        with open("books.bin", "rb+") as lib:
            try:
                while True:
                    book = pickle.load(lib)
                    if str(book.id) != id:
                        books.append(book)
            except EOFError:
                lib.seek(0)
                lib.truncate()
                for i in books:
                    pickle.dump(i, lib)

    def showBooks():
        lib= open("books.bin", "rb")
        try:
            while True:
                book= pickle.load(lib)
                print(f"ID: {book.id}")
                print(f"Name: {book.name}")
                print(f"Author: {book.author}")
                print(f"Publisher: {book.pub}")
                print(f"Price: {book.price}")
        except EOFError:
            print("Completed.")
            lib.close()
while True:
    print("1) Add book\n2) Remove book\n3) Show books\n4) Exit")
    ch= int(input("Your choice: ")[0])
    if ch==1:
        id= str(random.randint(1000,9999))
        print(f"Book ID: {id}")
        name= input("Book name: ")
        author= input("Author name: ")
        pub= input("Publisher: ")
        price= input("Price: ")
        book= Book(id, name, author, pub, price)
        Book.addBook(book)
    elif ch==2:
        Book.showBooks()
        id= input("Enter the ID of the book to remove: ")
        Book.removeBook(id)
    elif ch==3:
        Book.showBooks()
    else:
        print("Exitting.")
        break


