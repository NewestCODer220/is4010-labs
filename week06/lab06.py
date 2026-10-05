from datetime import date

class Book:
    """A book in a personal library."""
    
    def __init__(self, title: str, author: str, year: int):
        # Initialize the instance attributes
        self.title = title
        self.author = author
        self.year = year
        
    def __str__(self) -> str:
        # Provide a human-readable string including all three attributes
        return f"{self.title} by {self.author} ({self.year})"
        
    def get_age(self) -> int:
        """Return the number of years since publication."""
        # Use date.today().year to calculate the age
        return date.today().year - self.year

class EBook(Book):
    """An electronic version of a book with a file size."""
    
    def __init__(self, title: str, author: str, year: int, file_size: float):
        # Use super() to let the parent class handle the first three attributes
        super().__init__(title, author, year)
        
        # Add the new attribute unique to the child class
        self.file_size = file_size
        
    def __str__(self) -> str:
        # Override the parent's __str__ to include the file size and "MB"
        return f"{self.title} by {self.author} ({self.year}) - {self.file_size}MB"    