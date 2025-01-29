class Book:
    """Initializing class `Book` with parameters `id`,`title`,`price` and `available`"""
    def __init__(self, id: int, title: str, price: float, available: bool):
        self._id = id
        self._title = title
        self._price = price
        self._available = available

    # Getters
    @property
    def id(self):
        return int(self._id)
    
    @property
    def title(self):
        return str(self._title)
    
    @property
    def price(self):
        return float(self._price)
    
    @property
    def available(self):
        return bool(self._available)

    # Setter
    @available.setter
    def available(self, status: bool):
        self._available = status

    def __str__(self) -> str:
        """Method used to print formated text when some object is called \
            without using other methods"""
        return ("ID: {}, Title: {}, ".format(self._id, self._title) +
              "Price: ${}, Available: {}".format(self._price, self._available))

class EBook(Book):
    """Initializing class `EBook` which inheris class `Book`"""
    def __init__(self, id: int, title: str, price: float, available: bool, file_size: float):
        # Using `super()` to call parent(`Book`) class method `__init__`
        super().__init__(id, title, price, available)
        self._file_size = file_size

    def __str__(self):
        """Method used to print formated text when some object is called \
            without using other methods"""
        return ("ID: {}, Title: {}, Price: ${}, ".format(self._id, self._title, self._price) +
              "Available: {}, File size: {} MB".format(self._available, self._file_size))

class Library:
    """Class `Library` responsible for methods `add_book`, `display_books` etc.
        It also contains book list"""
    def __init__(self, books):
        # `books` contatins list of object(books)
        self.books = books
    
    def add_book(self):
        """Method used to add books to book list\n
            It validates input(`id`, `title` etc.) as well"""
        print("Enter book details:")

        id_book = str(input("ID: "))
        if (check_int(id_book)):
            for i in range(len(self.books)):    # Checking for uniqueness
                if (self.books[i].id == int(id_book)):
                    return "ID is incorrect!"
        else:
            return "ID is incorrect!"
            
        title_book = str(input("Title: "))

        price_book = str(input("Price: ")).strip()
        try:
            if (float(price_book) >= 0):
                price_book = float(price_book)
            else:
                return "Price must be positive!"
        except ValueError:
            return "Price is incorrect!"
            
        available_book = str(input("Available (yes/no): ")).lower().strip()
        if (available_book == "yes"):
            available_book = True
        elif (available_book == "no"):
            available_book = False
        else:
            return ("Available is incorrect!")
        
        is_ebook = str(input("E-book (yes/no): ")).lower().strip()
        if (is_ebook == "yes"):
            is_ebook = True
            size = str(input("Enter file size (in MB): ")).strip()
            try:
                if (float(size) >= 0):
                    size = float(size)
                else:
                    return "Size must be positive!"
            except ValueError:
                return "Size is incorrect!"
        elif (is_ebook == "no"):
            is_ebook = False
        else:
            return ("Value is incorrect!")
        
        # If book is electronic then creates object instance 
        # that inherits Book but have `file_size` variable
        # Otherwise, creates common book
        if (is_ebook):
            book = EBook(id_book, title_book, price_book, available_book, size)
        else:
            book = Book(id_book, title_book, price_book, available_book)

        # Adding object `book` to book list
        self.books.append(book)
        return "Book \"{}\" added successfully!".format(title_book)
    
    def borrow_book(self, id_book):
        """Method used to borrow book and change `available` variable in objects"""
        for book in self.books:
            if (book.id == int(id_book)):
                if (book.available):
                    book.available = False
                    return "Book \"{}\" borrowed successfully!".format(book.title)
                return "Book is not available!"
        return "Book is not found!"
        
    def return_book(self, id_book):
        """Method used to return book and change `available` variable in objects"""
        for book in self.books:
            if (book.id == int(id_book)):
                if (not book.available):
                    book.available = True
                    return "Book \"{}\" returned successfully!".format(book.title)
                return "Book is already in the library!"
        return "Book is not found!"

    def display_books(self):
        """Method used to display all books from book list"""
        print("Books in the library:")
        for i in range(len(self.books)):
            print("{}. {}".format(i+1, self.books[i]))

    def find_books_by_title(self, keyword: str, i = 1):
        """Methods used to searche for books containing a specific 
            keyword (case-insensitive) in their title."""
        print("Books matching your search:")
        for book in self.books:
            if (keyword in book.title.strip().lower()):
                print("{}. {}".format(i, book))
                i += 1

    def sort_books_by_price(self, ascending = True,):
        """Method used to sort the list of books by price in ascending 
            or descending order and display the list"""
        print("Books sorted by price:")
        sorted_books = sorted(self.books, key=lambda s: s.price, reverse=not ascending)
        for i in range(len(sorted_books)):
            print("{}. {}".format(i+1, sorted_books[i]))

def check_int(any_int: str):
    """Function that validates integer value"""
    if (any_int.isnumeric()):
        if (int(any_int) >= 0):
            return True
        print("The value must be positive!")
        return False
    print("The value is incorrect!")
    return False

if __name__ == "__main__":
    print("Welcome to the Mini Library System!\n")
    print("Menu:\n" +
        "1. Add a book\n" +
        "2. Display all books\n" +
        "3. Borrow a book\n" +
        "4. Return a book\n" +
        "5. Search for books by title\n" +
        "6. Sort books by price\n" +

        "7. Exit")
    
    # Creates object lib to interact with methods
    lib = Library(list())
    while True:
        cmd = str(input("\nYour choice: ")).strip()
        match (cmd):
            case '1':   # 1. Add a book.
                print(lib.add_book())
            case '2':   # 2. Display all books.
                lib.display_books()
            case '3':   # 3. Borrow a book.
                id_book = str(input("Enter book ID to borrow: ")).strip()
                if (check_int(id_book)):
                    print(lib.borrow_book(id_book))
            case '4':   # 4. Return a book.
                id_book = str(input("Enter book ID to return: ")).strip()
                if (check_int(id_book)):
                    print(lib.return_book(id_book))
            case '5':   # 5. Search for books by title.
                title = str(input("Enter keyword to search for: ")).strip().lower()
                lib.find_books_by_title(title)
            case '6':   # 6. Sort books by price.
                asc = str(input("Sort books by price (ascending/descending): ")).lower().strip()
                if (asc == "ascending" or asc == "asc"):
                    lib.sort_books_by_price(True)
                elif (asc == "descending" or asc == "desc"):
                    lib.sort_books_by_price(False)
                else:
                    print("The input is incorrect!")
            case '7':   # 6. Exit.
                print("Thank you for using the Mini Library System!")
                break
            case _:     # Exception
                print("Unknown command!")