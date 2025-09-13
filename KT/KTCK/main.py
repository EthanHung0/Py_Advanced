from book_module import Book
from library_module import Library
import time


def main():
    Ruina = Library()

    while True:
        print("""
|--------------------------------------------------|
|               The Library Of Ruina               |
|--------------------------------------------------|
| 1. Add books.                                    |
| 2. Books presentation.                           |
| 3. Total book amount.                            |
| 4. Find book.                                    |
| 5. Remove book by Title.                         |
| 6. Exit.                                         |
|--------------------------------------------------|
""")
        choice = input("Select a functionality (1-6): ")

#---------------------------------------------------------------------------------------------------

        if choice == "1": # add
            try:

                try:
                    amount = int(input("Input the amount of adding books: "))
                except ValueError:
                    raise ValueError("The amount of books must be an intger value.")
                if amount < 0:
                    raise ValueError("The amount of books musn't be lower than 0.")

                for _ in range(amount):
                    book_title = input("Input the Title of the book: ")
                    book_author = input("Input the Author of the book: ")
                    book_year = input("Input the book's releasing year (4 digits or lower): ")
                    Ruina.addBook(Book(book_title, book_author, book_year))

            except ValueError as e:
                print(f"Error while adding book{"s" if amount > 1 else ""}: {e}")
                time.sleep(0.5)

            print("Counting books...")
            time.sleep(0.5)
            print(f"Reception of books ended ({Ruina.count_books()} books were added).")
            input(">")

#---------------------------------------------------------------------------------------------------

        elif choice == "2": # show
            Ruina.listBooks()
            input(">")

#---------------------------------------------------------------------------------------------------

        elif choice == "3": # count
            print("Counting books...")
            time.sleep(0.5)
            print(f"Total available Books: {Ruina.count_books()}")
            input(">")

#---------------------------------------------------------------------------------------------------

        elif choice == "4": # find
            try:
                choose = input("Select a viable finding method (Title/Author): ").lower()
                if choose == "title":
                    titlef = input("Input finding Book's title: ")
                elif choose == "author":
                    authorf = input("Input finding book(s)' author: ")
                else:
                    raise ValueError("Invalid selection.")

                print(f"Found Book: {Ruina.findByTitle(titlef) if choose == "title" else Ruina.findByAuthor(authorf)}.")

            except ValueError as e:
                print(f"Error while finding book: {e}")

#---------------------------------------------------------------------------------------------------

        elif choice == "5": # remove
            try:
                r_title = input("Input removing book's title: ")
                Ruina.remove_book(r_title)

                print("Processing removal...")
                time.sleep(0.5)
                print(f'The book "{r_title}" has been removed from The Library.')
                time.sleep(0.5)

            except ValueError as e:
                print(f"Error while removing book: {e}")

#---------------------------------------------------------------------------------------------------

        elif choice == "6": # exit
            print("Closing the library...")
            time.sleep(0.5)

#---------------------------------------------------------------------------------------------------

        else:
            print("Invalid choice.")
            time.sleep(0.5)




main()