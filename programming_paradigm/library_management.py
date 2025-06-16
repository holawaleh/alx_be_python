# library_management.py

class Book:
    """Represents a book in the library with availability tracking."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute for checkout status

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True
    
    def return_book(self):
        """Mark the book as returned (available)."""
        self._is_checked_out = False
    
    @property
    def is_available(self):
        """Return availability status of the book."""
        return not self._is_checked_out


class Library:
    """Manages a collection of books with checkout/return functionality."""
    
    def __init__(self):
        self._books = []  # Private list to store book instances

    def add_book(self, book):
        """Add a new book to the library collection."""
        self._books.append(book)
    
    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title == title and book.is_available:
                book.check_out()
                return
    
    def return_book(self, title):
        """Return a checked-out book by title."""
        for book in self._books:
            if book.title == title and not book.is_available:
                book.return_book()
                return
    
    def list_available_books(self):
        """Print all currently available books."""
        for book in self._books:
            if book.is_available:
                print(f"{book.title} by {book.author}")
