# Task Nr.4:

# Create a class to represent a library system. The library system should have a collection of books that can be borrowed by users.
#  Users can register to the library system, borrow books, and return books.
#  The library system should keep track of the books borrowed by users, and the number of available copies of each book.


# Sukurkite klasę, kuri atstovautų bibliotekos sistemai. Bibliotekų sistemoje turėtų būti knygų kolekcija, kurią vartotojai galėtų pasiskolinti.
# Vartotojai gali registruotis bibliotekos sistemoje, skolintis ir grąžinti knygas.
# Bibliotekos sistema turėtų sekti vartotojų pasiskolintas knygas ir turimų kiekvienos knygos kopijų skaičių.
# pylint: disable= missing-docstring
import hashlib


class Book:
    def __init__(self, title: str, copies: int) -> None:
        self.title = title
        self.copies = copies


class User_registration:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        self.books_taken: list = []


class Library_system:
    BOOKS: list = []
    USERS: list = []

    @classmethod
    def add_user(cls, user) -> None:
        cls.USERS.append(user)

    @classmethod
    def add_book(cls, book) -> None:
        cls.BOOKS.append(book)

    @classmethod
    def get_books(cls) -> list:
        return cls.BOOKS

    @classmethod
    def get_users(cls) -> list:
        return cls.USERS

    @classmethod
    def take_book(cls, book_title, user) -> str:
        for book in cls.BOOKS:
            if book.title == book_title:
                if book.copies == 0:
                    return "Nera daugiau šios knygos imk kita..."
                else:
                    book.copies -= 1
                    user.books_taken.append(book.title)
                    return f"gero skaitymo, {user.username}"
        return "Nera tokios knygos pas mus"

    @classmethod
    def return_book(cls, book_title, user) -> str:
        for book in user.books_taken:
            if book == book_title:
                user.books_taken.remove(book_title)
                for copies in cls.BOOKS:
                    if copies.title == book_title:
                        copies.copies += 1
                        return "Aciu , kad grazinai"

        return "Neturi tokios knygos..."


book1 = Book(title="Book1", copies=10)
book2 = Book(title="Book2", copies=10)
Library_system.add_book(book1)
Library_system.add_book(book2)

books = Library_system.get_books()
for book in books:
    print(f"Title: {book.title}, copies: {book.copies}")

user1 = User_registration(username="Danielius", password="password")
user2 = User_registration(username="Antanas", password="Antano")
user3 = User_registration(username="Margis", password="Burba")
Library_system.add_user(user1)
Library_system.add_user(user2)
Library_system.add_user(user3)
users = Library_system.get_users()
for user in users:
    print(
        f"User: {user.username}, password: {hashlib.sha256(user.password.encode('utf-8')).hexdigest()}, taken books: {user.books_taken}"
    )

Library_system.take_book("Book2", user1)

books = Library_system.get_books()
for book in books:
    print(f"Title: {book.title}, copies: {book.copies}")

users = Library_system.get_users()
for user in users:
    print(
        f"User: {user.username}, password: {hashlib.sha256(user.password.encode('utf-8')).hexdigest()}, taken books: {user.books_taken}"
    )

print(Library_system.take_book("Book1", user1))
print(Library_system.take_book("Book2", user1))
print(Library_system.take_book("Book1", user1))
print(Library_system.take_book("Book2", user2))
print(Library_system.take_book("Book5", user2))

books = Library_system.get_books()
for book in books:
    print(f"Title: {book.title}, copies: {book.copies}")

users = Library_system.get_users()
for user in users:
    print(
        f"User: {user.username}, password: {hashlib.sha256(user.password.encode('utf-8')).hexdigest()}, taken books: {user.books_taken}"
    )

print(Library_system.return_book("Book5", user2))
print(Library_system.return_book("Book2", user2))
print(Library_system.return_book("Book2", user2))

books = Library_system.get_books()
for book in books:
    print(f"Title: {book.title}, copies: {book.copies}")

users = Library_system.get_users()
for user in users:
    print(
        f"User: {user.username}, password: {hashlib.sha256(user.password.encode('utf-8')).hexdigest()}, taken books: {user.books_taken}"
    )
