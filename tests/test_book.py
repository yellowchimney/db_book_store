from lib.book import Book

def test_book_has_attributes():
    book = Book(1, 'test_book', 'test_author')

    assert book.id == 1
    assert book.title == 'test_book'
    assert book.author == 'test_author'

def test_book_formats_nicely():
    book = Book(1, 'test_book', 'test_author')

    assert str(book) == 'Book(1, test_book, test_author)'

def test_equality():
    book1 = Book(1, 'test_book', 'test_author')
    book2 = Book(1, 'test_book', 'test_author')

    assert book1 == book2