# Norėdami tvarkyti knygų sąrašą bibliotekoje, turite sukurti programą.
# Kiekviena knyga turi pavadinimą, autorių, išleidimo metus ir ISBN.
# Turite apibrėžti knygų klasę naudodami duomenų klasės modulį, kuriame yra šių savybių atributai.
# Taip pat turite įdiegti biblioteką, kuri tvarko knygų sąrašą. Bibliotekos klasė turėtų leisti jums pridėti ir pašalinti knygas iš bibliotekos,
# ieškokite knygų pagal pavadinimą arba autorių ir parodykite šiuo metu bibliotekoje esančių knygų sąrašą.


# You need to create a program to manage a list of books in a library.
# Each book has a title, an author, a publication year, and an ISBN.
# You need to define a Book class using the dataclass module that contains attributes for these properties.
#  You also need to implement a Library class that manages a list of books. The Library class should allow you to add and remove books from the library,
#   search for books by title or author, and display the list of books currently in the library.


from dataclasses import dataclass
from typing import List
from collections.abc import Iterator

class Library:
    BOOKS: List = []

    def add_book(self, book) -> str:
        self.BOOKS.append(book)
        return f"Pridėta {book.title}"

    def remove_book(self, ISBN:int) -> str:
        for i, book in enumerate(self.BOOKS):
            if book.ISBN == ISBN:
                del self.BOOKS[i]
                return f"Ištrinta tokia knyga su ISBN: {ISBN} kodu"
        return "Neradau tokio ISBN"

    @classmethod
    def search_books_by_title(cls, title: str) -> str:
        for book in cls.BOOKS:
            if book.title == title:
                return f"Title: {book.title}, Author: {book.author}, Publication_year: {book.publication_year}, ISBN: {book.ISBN}"
        return f"Neradau tokios knygos pavadinimo: {title}"

    @classmethod
    def search_books_by_author(cls, author: str) -> str:
        for book in cls.BOOKS:
            if book.author == author:
                return f"Title: {book.title}, Author: {book.author}, Publication_year: {book.publication_year}, ISBN: {book.ISBN}"
        return f"Neradau tokios knygos pagal toki autoriu: {author}"

    @classmethod
    def show_books(cls) ->Iterator[str]:
        for book in cls.BOOKS:
            yield f"Title: {book.title}, Author: {book.author}, Publication_year: {book.publication_year}, ISBN: {book.ISBN}"


@dataclass
class Book(Library):
    title: str
    author: str
    publication_year: int
    ISBN: int


book5 = Book(title="Harr5", author="rowling", publication_year=2000, ISBN=2191915)
book1 = Book(title="Harry", author="rowling", publication_year=2023, ISBN=2191919195)
book2 = Book(
    title="Harry2", author="rowling", publication_year=2022, ISBN=2119192222225
)
book3 = Book(title="Harry3", author="rowling", publication_year=2021, ISBN=211919225)
book4 = Book(
    title="TOKS SMAGUS AMŽIUS",
    author="Kiley Reid",
    publication_year=2023,
    ISBN=9786094873713,
)
print(book1.add_book(book1))
print(book2.add_book(book2))
print(book3.add_book(book3))
print(book4.add_book(book4))
print(book5.add_book(book5))

print(book1.remove_book(ISBN=2191919195))


print(Library.search_books_by_title(title="Harry2"))

print(Library.search_books_by_author(author="Kiley Reid"))

all_books = Library.show_books()
for book in all_books:
    print(book)
