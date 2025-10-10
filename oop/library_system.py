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
    def __init__(self, book):
        self.books = book
        self.books = []

    def add_books(self, books):
        self.books.append(Book)
        self.books.append(EBook)
        self.books.append(PrintBook)

    def list_books(self):
        print(self.books)