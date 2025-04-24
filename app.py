from lib.db_connection import DatabaseConnection
from lib.book_repo import BookRepo

connection = DatabaseConnection()
connection.connect()
connection.seed('seeds/books.sql')

book_repo = BookRepo(connection)
books = book_repo.all()

for book in books:
    print(book)