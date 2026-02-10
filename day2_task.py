#Create a single inheritance program for a Library system.
#Create a parent class named Book with:
#title
#author
#display_book_details() method
#Create a child class named IssuedBook that inherits from Book and adds:
#issued_to
#issued_date
#display_issued_book_details() method
#display_book_details() → shows only title and author
#display_issued_book_details() → shows title, author, issued_to, issued_date
#(it calls display_book_details() from the parent class using inheritance)
#Create one object of IssuedBook and display all details.

# Parent class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # Method to display only title and author
    def display_book_details(self):
        print("Title:", self.title)
        print("Author:", self.author)


# Child class
class IssuedBook(Book):
    def __init__(self, title, author, issued_to, issued_date):
        # Calling parent constructor
        super().__init__(title, author)
        self.issued_to = issued_to
        self.issued_date = issued_date

    # Method to display all issued book details
    def display_issued_book_details(self):
        # Calling parent class method
        super().display_book_details()
        print("Issued To:", self.issued_to)
        print("Issued Date:", self.issued_date)


# Creating one object of IssuedBook
book1 = IssuedBook(
    "Python Basics",
    "Guido van Rossum",
    "Moulya",
    "05-02-2026"
)

# Displaying all details
book1.display_issued_book_details()