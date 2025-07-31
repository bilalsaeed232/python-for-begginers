# Library Management System - OOP Example for Beginners
class Book:
    """Represents a book in the library"""
    
    def __init__(self, title, author, isbn):
        # Instance attributes - each book has these properties
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.borrowed_by = None
    
    def borrow(self, member_name):
        """Method to borrow a book"""
        if not self.is_borrowed:
            self.is_borrowed = True
            self.borrowed_by = member_name
            return f"'{self.title}' has been borrowed by {member_name}"
        else:
            return f"Sorry, '{self.title}' is already borrowed by {self.borrowed_by}"
    
    def return_book(self):
        """Method to return a book"""
        if self.is_borrowed:
            borrower = self.borrowed_by
            self.is_borrowed = False
            self.borrowed_by = None
            return f"'{self.title}' has been returned by {borrower}"
        else:
            return f"'{self.title}' was not borrowed"
    
    def get_info(self):
        """Method to get book information"""
        status = "Available" if not self.is_borrowed else f"Borrowed by {self.borrowed_by}"
        return f"Title: {self.title}, Author: {self.author}, Status: {status}"

class Member:
    """Represents a library member"""
    
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  # List to store borrowed books
    
    def borrow_book(self, book):
        """Method for member to borrow a book"""
        if len(self.borrowed_books) >= 3:
            return f"{self.name} cannot borrow more books (limit: 3)"
        
        result = book.borrow(self.name)
        if "has been borrowed" in result:
            self.borrowed_books.append(book)
        return result
    
    def return_book(self, book):
        """Method for member to return a book"""
        if book in self.borrowed_books:
            result = book.return_book()
            self.borrowed_books.remove(book)
            return result
        else:
            return f"{self.name} didn't borrow '{book.title}'"
    
    def display_all_members(self):
        """Method to show all members with their status"""
        if not self.me:
            return "No books in the library"
        
        print(f"\nAll books in {self.name}:")
        for book in self.books:
            print(f"- {book.get_info()}")

    def get_borrowed_books(self):
        """Method to see what books the member has borrowed"""
        if not self.borrowed_books:
            return f"{self.name} has no borrowed books"
        
        books_list = [book.title for book in self.borrowed_books]
        return f"{self.name}'s borrowed books: {', '.join(books_list)}"


class Library:
    """Represents the library system"""
    
    def __init__(self, name):
        self.name = name
        self.books = []      # List to store all books
        self.members = []    # List to store all members
    
    def add_book(self, book):
        """Method to add a book to the library"""
        self.books.append(book)
        return f"Added '{book.title}' to {self.name}"
    
    def add_member(self, member):
        """Method to add a member to the library"""
        self.members.append(member)
        return f"Added member: {member.name} (ID: {member.member_id})"
    
    def find_book(self, title):
        """Method to find a book by title"""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def find_member(self, member_id):
        """Method to find a member by ID"""
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
    
    def display_all_members(self):
        """Method to show all library members"""
        if not self.members:
            return "No members in the library"
        
        print(f"\nAll members of {self.name}:")
        for member in self.members:
            print(f"- ID: {member.member_id}, Name: {member.name}")

    def display_available_books(self):
        """Method to show all available books"""
        available_books = [book for book in self.books if not book.is_borrowed]
        
        if not available_books:
            return "No books available"
        
        print(f"\nAvailable books in {self.name}:")
        for book in available_books:
            print(f"- {book.get_info()}")
    
    def display_all_books(self):
        """Method to show all books with their status"""
        if not self.books:
            return "No books in the library"
        
        print(f"\nAll books in {self.name}:")
        for book in self.books:
            print(f"- {book.get_info()}")


class LibraryInterface:
    """Handles all user interface operations for the library system"""
    
    def __init__(self, library):
        self.library = library
    
    def display_menu(self):
        """Display the main menu options"""
        print("\n" + "="*40)
        print("    LIBRARY MANAGEMENT SYSTEM")
        print("="*40)
        print("1. Add a new book")
        print("2. Add a new member")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Display all books")
        print("6. Display available books")
        print("7. Display member's borrowed books")
        print("8. Display all members")
        print("9. Search for a book")
        print("10. Exit")
        print("="*40)

    def get_user_choice(self):
        """Get and validate user's menu choice"""
        while True:
            try:
                choice = int(input("Enter your choice (1-10): "))
                if 1 <= choice <= 10:
                    return choice
                else:
                    print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Please enter a valid number.")

    def add_book_menu(self):
        """Handle adding a new book"""
        print("\n--- Add New Book ---")
        title = input("Enter book title: ").strip()
        author = input("Enter book author: ").strip()
        isbn = input("Enter book ISBN: ").strip()
        
        if title and author and isbn:
            new_book = Book(title, author, isbn)
            result = self.library.add_book(new_book)
            print(f"✓ {result}")
        else:
            print("❌ All fields are required!")

    def add_member_menu(self):
        """Handle adding a new member"""
        print("\n--- Add New Member ---")
        name = input("Enter member name: ").strip()
        member_id = input("Enter member ID: ").strip()
        
        if name and member_id:
            # Check if member ID already exists
            if self.library.find_member(member_id):
                print("❌ Member ID already exists!")
                return
            
            new_member = Member(name, member_id)
            result = self.library.add_member(new_member)
            print(f"✓ {result}")
        else:
            print("❌ All fields are required!")

    def borrow_book_menu(self):
        """Handle borrowing a book"""
        print("\n--- Borrow Book ---")
        member_id = input("Enter your member ID: ").strip()
        book_title = input("Enter book title: ").strip()
        
        member = self.library.find_member(member_id)
        book = self.library.find_book(book_title)
        
        if not member:
            print("❌ Member not found!")
            return
        
        if not book:
            print("❌ Book not found!")
            return
        
        result = member.borrow_book(book)
        if "has been borrowed" in result:
            print(f"✓ {result}")
        else:
            print(f"❌ {result}")

    def return_book_menu(self):
        """Handle returning a book"""
        print("\n--- Return Book ---")
        member_id = input("Enter your member ID: ").strip()
        book_title = input("Enter book title to return: ").strip()
        
        member = self.library.find_member(member_id)
        book = self.library.find_book(book_title)
        
        if not member:
            print("❌ Member not found!")
            return
        
        if not book:
            print("❌ Book not found!")
            return
        
        result = member.return_book(book)
        if "has been returned" in result:
            print(f"✓ {result}")
        else:
            print(f"❌ {result}")

    def display_member_books_menu(self):
        """Handle displaying member's borrowed books"""
        print("\n--- Member's Borrowed Books ---")
        member_id = input("Enter member ID: ").strip()
        
        member = self.library.find_member(member_id)
        if not member:
            print("❌ Member not found!")
            return
        
        result = member.get_borrowed_books()
        print(f"📚 {result}")

    def search_book_menu(self):
        """Handle searching for a book"""
        print("\n--- Search Book ---")
        title = input("Enter book title to search: ").strip()
        
        book = self.library.find_book(title)
        if book:
            print(f"📖 Found: {book.get_info()}")
        else:
            print("❌ Book not found!")

    def initialize_sample_data(self):
        """Add some sample data for testing"""
        # Add sample books
        books = [
            Book("The Python Tutorial", "Guido van Rossum", "123-456-789"),
            Book("Clean Code", "Robert Martin", "987-654-321"),
            Book("Automate the Boring Stuff", "Al Sweigart", "555-666-777"),
            Book("Python Crash Course", "Eric Matthes", "111-222-333")
        ]
        
        for book in books:
            self.library.add_book(book)
        
        # Add sample members
        members = [
            Member("Alice Johnson", "M001"),
            Member("Bob Smith", "M002"),
            Member("Carol Davis", "M003")
        ]
        
        for member in members:
            self.library.add_member(member)
        
        print("✓ Sample data loaded successfully!")