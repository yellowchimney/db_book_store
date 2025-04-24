class Book():
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author

    def __repr__(self):
        return f'Book({self.id}, {self.title}, {self.author})'
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__