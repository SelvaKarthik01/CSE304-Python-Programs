import csv

class Book:
    def __init__(self, title, author, genre, availability_status):
        self.title = title
        self.author = author
        self.genre = genre
        self.availability_status = availability_status

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, book):
        self.books[book_id] = book

    def remove_book(self, book_id):
        del self.books[book_id]

    def display_books(self):
        for book_id, book in self.books.items():
            print(f"Book ID: {book_id}")
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Genre: {book.genre}")
            print(f"Availability Status: {book.availability_status}")
            print()

    def search_book(self, query):
        results = []
        for book_id, book in self.books.items():
            if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                results.append(book)
        return results

    def update_availability(self, book_id, status):
        self.books[book_id].availability_status = status

    def save_library(self):
        with open("library.txt", "w") as f:
            json.dump(self.books, f)
            

    def load_library(self):
        try:
            with open("library.txt", "r") as f:
                self.books = json.load(f)
        except FileNotFoundError:
            print("No saved library found.")

def main():
    library = Library()
    library.load_library()

    while True:
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Display Books")
        print("4. Search Book")
        print("5. Update Availability")
        print("6. Save Library")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            availability_status = input("Enter availability status (Available/Unavailable): ")
            book_id = input("Enter book ID: ")
            book = Book(title, author, genre, availability_status)
            library.add_book(book_id, book)
        elif choice == 2:
            book_id = input("Enter book ID to remove: ")
            library.remove_book(book_id)
        elif choice == 3:
            library.display_books()
        elif choice == 4:
            query = input("Enter title or author to search: ")
            results = library.search_book(query)
            if results:
                for book in results:
                    print(f"Title: {book.title}")
                    print(f"Author: {book.author}")
                    print(f"Genre: {book.genre}")
                    print(f"Availability Status: {book.availability_status}")
                    print()
            else:
                print("No books found.")
        elif choice == 5:
            book_id = input("Enter book ID to update availability: ")
            status = input("Enter new availability status (Available/Unavailable): ")
            library.update_availability(book_id, status)
        elif choice == 6:
            library.save_library()
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
