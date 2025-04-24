from lib.book import Book
from lib.db_connection import DatabaseConnection

class BookRepo():
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM books')
        return [
            Book(row['id'], row['title'], row['author_name']) for row in rows
        ]
    
    def find(self, id):
        rows = self.connection.execute('SELECT * FROM books WHERE id = %s', [id])
        row = rows[0]
        return Book(row['id'], row['title'], row['author_name'])
       