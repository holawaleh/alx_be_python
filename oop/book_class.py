# book_class.py

class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor: Initializes the book attributes."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Prints a message when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Developer-friendly official string representation."""
        return f"Book('{self.title}', '{self.author}', {self.year})"


# Example usage (optional, can be removed in production)
if __name__ == "__main__":
    book1 = Book("1984", "George Orwell", 1949)
    print(str(book1))    # Informal output
    print(repr(book1))   # Official/developer output

    # Delete book explicitly to see the __del__ message
    del book1
