# Create a Library Management System where different library items calculate borrowing charges differently.
# Library item (parent class)
# Book and magazie (child class)
# LibraryApp(main class)

# Book IS-A libraryitem
# Magazine IS-A libraryitem
# LibraryApp HAS-A libraryitem

# Output format
# Item Type: Book
# Borrow Days: 5
# Borrowing Charge: 50
# Or 
# Item Type: Magazine
# Borrow Days: 3
# Borrowing Charge: 30 


# Parent class
class LibraryItem:
    def __init__(self, borrow_days):
        self.borrow_days = borrow_days

    def calculate_charge(self):
        pass


# Child class: Book
class Book(LibraryItem):
    def calculate_charge(self):
        return self.borrow_days * 10


# Child class: Magazine
class Magazine(LibraryItem):
    def calculate_charge(self):
        return self.borrow_days * 10


# Main class 
class LibraryApp:
    def __init__(self, item_type, borrow_days):
        if item_type.lower() == "book":
            self.item = Book(borrow_days)
            self.item_type = "Book"
        elif item_type.lower() == "magazine":
            self.item = Magazine(borrow_days)
            self.item_type = "Magazine"
        else:
            print("Invalid Item Type")
            return

        self.borrow_days = borrow_days

    def show_details(self):
        print(f"Item Type: {self.item_type}")
        print(f"Borrow Days: {self.borrow_days}")
        print(f"Borrowing Charge: {self.item.calculate_charge()}")



# For Book
l1 = LibraryApp("Book", 5)
l1.show_details()

print()

# For Magazine
l2 = LibraryApp("Magazine", 3)
l2.show_details()