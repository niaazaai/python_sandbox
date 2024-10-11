import json
import os
class Library:
    
    def __init__(self, filename='books.json'):
        self.filename = filename
        self.books = self.load_books()
    
    def load_books(self):
        """Load books from the JSON file."""
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    
    def save_books(self):
        """Save the current list of books to the JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.books, file, indent=4)
    
    def add_book(self, title, author):
        """Add a new book to the library."""
        book_id = self.generate_id() 
        new_book = {
            'id': book_id,
            'title': title,
            'author': author
        }
        self.books.append(new_book)
        self.save_books()
        print(f"Book added successfully with ID: {book_id}")
    
    def delete_book(self, book_id):
        """Delete a book from the library by its ID."""
        for book in self.books:
            if book['id'] == book_id:
                self.books.remove(book)
                self.save_books()
                print(f"Book with ID {book_id} has been deleted.")
                return
        print(f"No book found with ID {book_id}.")
    
    def view_books(self):
        """Display all books in the library."""
        if not self.books:
            print("No books available in the library.")
            return
        print("\nList of Available Books:")
        print("-" * 40)
        for book in self.books:
            print(f"ID: {book['id']}\nTitle: {book['title']}\nAuthor: {book['author']}\n")
        print("-" * 40)
    
    def generate_id(self):
        """Generate a unique ID for a new book."""
        if not self.books:
            return 1
        else:
            return max(book['id'] for book in self.books) + 1

def main():
    library = Library()
    
    while True:
        print("\nLibrary Management System")
        print("1. Add a Book")
        print("2. Delete a Book")
        print("3. View Available Books")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            title = input("Enter the book title: ").strip()
            author = input("Enter the book author: ").strip()
            if title and author:
                library.add_book(title, author)
            else:
                print("Title and Author cannot be empty.")
        
        elif choice == '2':
            try:
                book_id = int(input("Enter the book ID to delete: "))
                library.delete_book(book_id)
            except ValueError:
                print("Please enter a valid integer ID.")
        
        elif choice == '3':
            library.view_books()
        
        elif choice == '4':
            print("Exiting the Library Management System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

