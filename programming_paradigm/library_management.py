class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)


    def check_out_book(self, title):
        if not self.__is_checked_out:
            self.__is_checked_out = True
        else:
            return f"Book is already checked out"
        
    def return_book(self, title):
        "return_book(self)"
        if self.__is_checked_out:
            self.__is_checked_out = False
            return self.title
        
    def list_available_books(self):
        if not self.books:
            return "No books in the library."
        return self.books