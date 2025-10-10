class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        pass



class EBook(Book):
    def __init__(self, file_size):
        super().__init__()
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, page_count):
        super().__init__()
        self.page_count = page_count


class Library:
    def __init__(self, books):
        self.books = books
        self.books = []

    def add_books(self, books):
        if isinstance(books, Book):
            self.books.append(books)

    def list_books(self):
        print(self.books)