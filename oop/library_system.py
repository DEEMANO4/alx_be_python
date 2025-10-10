class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author



class EBOOK:
    def __init__(self, file_size):
        self.file_size = file_size

class PrintBook:
    def __init__(self, page_count):
        self.page_count = page_count


class library:
    def __init__(self, books):
        self.books = books

    def add_books(self, books):
        self.books.append(Book)
        self.books.append(EBOOK)
        self.books.append(PrintBook)

    def list_books(self):
        print(self.books)