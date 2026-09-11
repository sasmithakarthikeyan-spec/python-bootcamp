print("==========================")
print("LIBRARY MANAGEMENT SYSTEM")
print("==========================")

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.available=True

    def borrow(self):
        if self.available:
            self.available=False
            print("Book borrowed successfully")
        else:
            print("Book is not available")

    def return_book(self):
        self.available=True
        print("Book returned successfully")

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully")

    def show_books(self):
        for book in self.books:
            print("Title:", book.title)
            print("Author:", book.author)
            print("Available:", book.available)
            print("------------------")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                book.borrow()
                return

        print("Book not found")

    def return_book(self,title):
        for book in self.books:
            if book.title==title:
                book.return_book()
                return
        print("Book not found")


book1=Book("Python Basics","John Smith")
print(book1.title)
print(book1.author)
print(book1.available)

book1.borrow()
print(book1.available)

book1.borrow()

book1.return_book()
print(book1.available)

library = Library()

library.add_book(book1)

print(library.books)
library.show_books()

library.borrow_book("Python Basics")
library.show_books()

library.return_book("Python Basics")
library.show_books()