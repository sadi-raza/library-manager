import json
import os

data_file = 'library.text'

def load_books(file_path):
    """Load books from a JSON file."""
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as file:
        return json.load(file)
    
def save_books(file_path, books):
    """Save books to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(books, file, indent=4)

def add_book(books):
    """Add a new book to the library."""
    title = input("Enter book title: ")
    author = input("Enter book author: ")     
    year = input("Enter book year: ")
    genre = input("Enter book genre: ")
    read = input("Have you read this book? (yes/no): ").lower() == 'yes'

    book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }
    books.append(book)
    save_books(data_file, books)
    print(f"Book '{title}' added to the library.")

def remove_book(books, title):
    title = input("Enter the title of the book to remove: ")
    initial_length = len(books)
    books = [book for book in books if book['title'].lower() != title.lower()]
    if len(books) < initial_length:
        save_books(data_file, books)
        print(f"Book '{title}' removed from the library.")
    else:
        print(f"Book '{title}' not found in the library.")

def search_books(books):
    """Search for a book by title."""
    search_term = input("Enter the title of the book to search: ").lower()
    results = [book for book in books if search_term in book['title'].lower()]

    if results:
        for book in results:
            status = "Read" if book['read'] else "Not Read"
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Status: {status}")
    else:
        print(f"No books found matching '{search_term}'.")

def display_books(books):
    """Display all books in the library."""
    if  books:
        
     for book in books:
        status = "Read" if book['read'] else "Not Read"
        print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Status: {status}")
    else:
        print("No books in the library.")

def display_statistics(books):
    """Display statistics about the library."""
    total_books = len(books)
    read_books = len(list(book for book in books if book['read']))
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0

    
    print(f"Total books: {total_books}")
    print(f"Read books: {percentage_read:.2f}%")

def main():
    """Main function to run the library manager."""
    books = load_books(data_file)

    while True:
        print("Menu")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Books")
        print("4. Display All Books")
        print("5. Display Statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_book(books)
        elif choice == '2':
            remove_book(books)
        elif choice == '3':
            search_books(books)
        elif choice == '4':
            display_books(books)
        elif choice == '5':
            display_statistics(books)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()



