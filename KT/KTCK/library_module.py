from book_module import Book


class Library:
    def __init__(self):
        self._books : list[Book] = []


    def addBook(self,book:Book):
        self._books.append(book)


    def listBooks(self):
        if not self._books:
            print("Library is empty.")
            return
        print("\n|-------------------- Available books --------------------|\n")
        for i,book in enumerate(self._books, 1):
            print(f"| {i}. {book}")
        print("|---------------------------------------------------------|\n")


    def findByTitle(self, titlef:str) -> Book:
        if not self._books:
            print("Library is empty.")
            return
        for book in self._books:
            if book.title.lower() == titlef.lower(): return book
        raise ValueError(f'Book "{titlef}" not found.')


    def findByAuthor(self, authorf:str) -> Book:
        if not self._books:
            print("Library is empty.")
            return
        book_list = []
        for book in self._books:
            if book.author.lower() == authorf.lower():
                book_list.append(book)
                return book_list
        raise ValueError(f'Book by author "{authorf}" not found.')


    def remove_book(self,r_title:str):
        self._books.remove(self.findByTitle(r_title))


    def count_books(self) -> int:
        return len(self._books)
