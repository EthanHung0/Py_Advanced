
class BookNotFoundError(Exception):
    def __init__(self,book):
        super().__init__(f"Book {book} not found.")

class OutOfStockError(Exception):
    def __init__(self):
        super().__init__("Library is out of stock.")


class Book:
    def __init__(self,name:str,author:str,pages:int):
        self.name = name
        self.author = author
        self.pages = pages

class Library:
    def __init__(self):
        self._books = []

    def addBook(self,book:Book):
        self._books.append(book)

    def borrowBook(self,book:Book):
        if not self._books:
            raise OutOfStockError()
        for b in self._books:
            if b == book:
                self._books.remove(b)
                return book
        raise BookNotFoundError(book)