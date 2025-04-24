from lib.book import Book
from lib.db_connection import DatabaseConnection
from lib.book_repo import BookRepo

def test_all_returns_all_books(db_connection):
    # connection = DatabaseConnection()
    db_connection.seed('seeds/books.sql')
    repo = BookRepo(db_connection)

    books = repo.all()

    assert books == [
        Book(1,'Nineteen Eighty-Four', 'George Orwell'),
        Book(2,'Mrs Dalloway', 'Virginia Woolf'),
        Book(3,'Emma', 'Jane Austen'),
        Book(4,'Dracula', 'Bram Stoker'),
        Book(5,'The Age of Innocence', 'Edith Wharton')
    ]

def test_find_returns_one_book(db_connection):
    db_connection.seed('seeds/books.sql')
    repo = BookRepo(db_connection)

    book = repo.find(2)

    assert book == Book(2,'Mrs Dalloway', 'Virginia Woolf')
