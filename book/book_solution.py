# This solution demonstrates fundamental OOP concepts using a Book class.
# There are multi-line comments (inbetween  the double quotes: """ and """ ) that attempt to explain the code. 

class Book:
    """
    A class representing a book in a library.
    
    This class demonstrates core OOP concepts:
    - Encapsulation: Book data and behaviors are bundled together
    - Attributes: Instance variables that store book properties
    - Methods: Functions that define book behaviors
    
    Attributes:
        title (str): The title of the book
        author (str): The author of the book
        pages (int): The number of pages in the book
        is_available (bool): Whether the book is available for checkout
    """
  
    def __init__(self, title, author, pages):
        """
        Initialize a new Book object.
        
        The constructor (__init__) is called when creating a new Book object.
        It sets up the initial state of the book by assigning values to instance
        attributes. Each attribute is prefixed with 'self.' to indicate it belongs
        to this specific instance.
        
        Args:
            title (str): The book's title
            author (str): The book's author
            pages (int): Number of pages in the book
        """
        # Store the passed parameters as instance attributes
        self.title = title
        self.author = author
        self.pages = pages
        # Set initial availability to True (book starts as available)
        self.is_available = True
    
    def checkout(self):
        """
        Attempt to check out the book.
        
        This method implements the checkout behavior using a conditional statement
        to check the current availability status. It demonstrates state management
        within a class method.
        
        Returns:
            bool: True if checkout was successful, False if book was unavailable
        """
        # Check if the book is available for checkout
        if self.is_available:
            # If available, mark as checked out and return success
            self.is_available = False
            return True
        else:
            # If not available, return failure
            return False
    
    def return_book(self):
        """
        Process a book return.
        
        This method is simpler than checkout() as we always allow returns.
        It demonstrates how methods can modify instance state.
        
        Returns:
            bool: True to indicate successful return
        """
        # Mark the book as available again
        self.is_available = True
        # Return success
        return True
    
    def get_info(self):
        """
        Create a string representation of the book's information.
        
        This method demonstrates string formatting and conditional text generation
        based on instance attributes. It uses an f-string for clean string
        interpolation.
        
        Returns:
            str: Formatted string containing book information
        """
        # Convert boolean availability to user-friendly string
        if self.is_available:
            availability_status = "Available"  
        else:
            availability_status = "Not Available"
        
        # Create and return formatted string using f-string
        return f"{self.title} by {self.author} ({self.pages} pages) - {availability_status}"


def test_book_class():
    """
    Test the Book class implementation.
    
    This function demonstrates how to:
    1. Create class instances
    2. Call methods on objects
    3. Test different scenarios
    4. Print results for verification
    """
    
    # Get user input for book details
    print("\n=== Testing my Book Class ===")
    title = input("Enter the book name: ")
    author = input("Enter the author name: ")
    pages = int(input("Enter the number of pages: "))
    
    # Create a new book instance
    book = Book(title, author, pages)
    
    # Test 1: Initial state
    print("\nTest 1: Initial state")
    print("Initial book info:", book.get_info())
    
    # Test 2: Successful checkout
    print("\nTest 2: First checkout attempt")
    success = book.checkout()
    print("Checkout successful?", success)
    print("After checkout:", book.get_info())
    
    # Test 3: Failed checkout (book already checked out)
    print("\nTest 3: Second checkout attempt")
    success = book.checkout()
    print("Second checkout successful?", success)
    
    # Test 4: Return
    print("\nTest 4: Return book")
    success = book.return_book()
    print("Return successful?", success)
    print("After return:", book.get_info())
    if succcess:
      print("It worked and I am awesome!")

if __name__ == "__main__":
    # Run the test function when the script is executed
    test_book_class()
