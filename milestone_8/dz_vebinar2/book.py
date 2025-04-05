from dataclasses import dataclass, field
from typing import List
from collections import defaultdict

@dataclass
class Book:
    title: str
    author: str
    category: str

@dataclass
class Shelf:
    id: int
    books: List[Book] = field(default_factory=list)

    def add_book(self, book: Book):
        self.books.append(book)

    def sort_books(self):
        self.books.sort(key=lambda b: b.title)

@dataclass
class Room:
    shelves: List[Shelf] = field(default_factory=list)

    def organize_books_by_category(self, books: List[Book]):
        category_to_books = defaultdict(list)
        for book in books:
            category_to_books[book.category].append(book)

        shelf_id = 1
        for category_books in category_to_books.values():
            shelf = Shelf(id=shelf_id)
            for book in category_books:
                shelf.add_book(book)
            self.shelves.append(shelf)
            shelf_id += 1

    def sort_books_on_shelves(self):
        for shelf in self.shelves:
            shelf.sort_books()

def main():
    books = [
        Book("The Hobbit", "J.R.R. Tolkien", "Fantasy"),
        Book("A Game of Thrones", "George R.R. Martin", "Fantasy"),
        Book("Sapiens", "Yuval Noah Harari", "History"),
        Book("1984", "George Orwell", "Dystopia"),
        Book("Brave New World", "Aldous Huxley", "Dystopia"),
    ]

    room = Room()
    room.organize_books_by_category(books)
    room.sort_books_on_shelves()

    for shelf in room.shelves:
        print(f"\nShelf {shelf.id}:")
        for book in shelf.books:
            print(f" - {book.title} by {book.author} [{book.category}]")

if __name__ == "__main__":
    main()
