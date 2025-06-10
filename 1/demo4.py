# **Object-Oriented Programming (OOP) in Python - Detailed Guide with Programs**

## **1. Introduction to OOP**
'''Object-Oriented Programming (OOP) is a programming paradigm that organizes code into **objects** containing both **data (attributes)** and **behavior (methods)**. The four main pillars of OOP are:

1. **Encapsulation**: Bundling data and methods that operate on that data.
2. **Abstraction**: Hiding complex details while exposing essential features.
3. **Inheritance**: Creating new classes from existing ones.
4. **Polymorphism**: Using a single interface for different data types.
'''

## **2. Classes and Objects**
### **Class**
#A blueprint for creating objects. It defines attributes and methods.

### **Object**
#An instance of a class.


### **Example 1: Basic Class and Object**
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    # Instance attributes (unique to each object)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        print(f"{self.name} says Woof!")

# Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Milo", 5)

# Access attributes and methods
print(dog1.name)        # Output: Buddy
Dog.species="Lab"
print(dog1.species)    # Output: Canis familiaris
dog1.bark()             # Output: Buddy says Woof!


## **3. Encapsulation**
#Bundling data and methods that work on that data, restricting direct access to some components.

### **Example 2: Encapsulation with Private Attributes**
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds!")

    def get_balance(self):  # Getter method
        return self.__balance

# Usage
account = BankAccount("Alice", 100)
account.deposit(50)       # Deposited $50. New balance: $150
account.withdraw(200)     # Insufficient funds!
print(account.get_balance())  # 150
# account.__balance  # Error: AttributeError (private)



## **4. Inheritance**
#Creating a new class from an existing class to reuse code.

### **Example 3: Single Inheritance**
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Usage
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!




## **5. Polymorphism**
#Using a unified interface for different data types.

### **Example 4: Polymorphism with Methods**

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Polymorphic function
def print_area(shape):
    print(f"Area: {shape.area()}")

# Usage
rect = Rectangle(4, 5)
circle = Circle(7)
print_area(rect)    # Output: Area: 20
print_area(circle)  # Output: Area: 153.86


## **6. Abstraction**
#Hiding complex implementation details.

### **Example 5: Abstract Base Class**

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

# Usage
square = Square(5)
print(square.area())      # Output: 25
print(square.perimeter()) # Output: 20
# shape = Shape()  # Error: Can't instantiate abstract class


## **7. Advanced OOP Concepts**
### **Class Methods & Static Methods**

class MyClass:
    class_var = "Class Variable"

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method")

# Usage
MyClass.class_method()  # Output: Called class_method of <class '__main__.MyClass'>
MyClass.static_method() # Output: Called static_method


## **8. Real-World Project: Library Management System**

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return True
        return False

    def return_book(self):
        if self.checked_out:
            self.checked_out = False
            return True
        return False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

# Usage
library = Library()
book1 = Book("Python 101", "John Doe", "12345")
library.add_book(book1)

found = library.find_book("12345")
if found and found.check_out():
    print(f"Checked out: {found.title}")



'''

## **Key Takeaways**
1. **Classes** are blueprints, **objects** are instances.
2. **Encapsulation** protects data via access control.
3. **Inheritance** promotes code reuse.
4. **Polymorphism** allows flexible method calls.
5. **Abstraction** simplifies complex systems.

Each example builds on previous concepts, showing how OOP makes code more organized and maintainable. Try extending these examples with your own features!'''

'''
# **Day 7: Object-Oriented Programming (OOP) - Extended Explanation**

## **1. Constructor (`__init__`) and `self`**
### **Constructor (`__init__`)**
- Special method that runs automatically when an object is created
- Used to initialize object attributes
- Syntax: `def __init__(self, parameters):`

### **`self` Parameter**
- Refers to the current instance of the class
- Must be the first parameter in instance methods
- Used to access instance variables and methods
'''
class Car:
    def __init__(self, brand, model):
        # Instance attributes
        self.brand = brand
        self.model = model
        self.speed = 0  # Default value
    
    def accelerate(self, increase):
        self.speed += increase
        print(f"Accelerating to {self.speed} km/h")

# Create objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

car1.accelerate(20)  # Output: Accelerating to 20 km/h

'''
## **2. Class vs Instance Attributes**
### **Class Attributes**
- Shared by all instances
- Defined outside any method
- Accessed using class name or instance

### **Instance Attributes**
- Unique to each instance
- Defined inside `__init__` or other methods
- Accessed only through instance
'''
class Employee:
    # Class attribute
    company = "TechCorp"
    
    def __init__(self, name, position):
        # Instance attributes
        self.name = name
        self.position = position

# Usage
emp1 = Employee("Alice", "Developer")
emp2 = Employee("Bob", "Manager")

print(emp1.company)  # Output: TechCorp (class attribute)
print(Employee.company)  # Output: TechCorp
emp1.company = "NewCorp"  # Creates instance attribute
print(emp1.company)  # Output: NewCorp (instance attribute)
print(emp2.company)  # Output: TechCorp (still class attribute)

'''
## **3. BankAccount Class Exercise**
### **Requirements**
- Attributes: `owner`, `balance`
- Methods:
  - `deposit(amount)`: Add to balance
  - `withdraw(amount)`: Subtract from balance (check for sufficient funds)
  - `display_balance()`: Print current balance
'''
### **Solution**
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
    
    def display_balance(self):
        print(f"Account owner: {self.owner}")
        print(f"Current balance: ${self.balance}")

# Usage
account = BankAccount("John Doe", 1000)
account.deposit(500)    # Deposited $500. New balance: $1500
account.withdraw(200)   # Withdrew $200. New balance: $1300
account.withdraw(2000)  # Insufficient funds!
account.display_balance()

'''
## **4. Inventory System Project**
### **Requirements**
- Track items with quantities
- Methods:
  - `add_item(item, quantity)`: Add/update inventory
  - `remove_item(item, quantity)`: Remove items (check availability)
  - `display_inventory()`: Show all items
'''
### **Solution**

class Inventory:
    def __init__(self):
        self.items = {}  # Dictionary to store items
    
    def add_item(self, item, quantity=1):
        if quantity <= 0:
            print("Quantity must be positive")
            return
        
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
        print(f"Added {quantity} {item}(s)")
    
    def remove_item(self, item, quantity=1):
        if item not in self.items:
            print(f"{item} not in inventory")
            return
        
        if quantity <= 0:
            print("Quantity must be positive")
            return
        
        if self.items[item] < quantity:
            print(f"Not enough {item} in stock")
            return
        
        self.items[item] -= quantity
        if self.items[item] == 0:
            del self.items[item]
        print(f"Removed {quantity} {item}(s)")
    
    def display_inventory(self):
        if not self.items:
            print("Inventory is empty")
            return
        
        print("\nCurrent Inventory:")
        for item, quantity in self.items.items():
            print(f"- {item}: {quantity}")

# Usage
store = Inventory()
store.add_item("Laptop", 5)     # Added 5 Laptop(s)
store.add_item("Mouse", 10)     # Added 10 Mouse(s)
store.add_item("Laptop", 3)     # Added 3 Laptop(s)
store.remove_item("Mouse", 2)   # Removed 2 Mouse(s)
store.remove_item("Keyboard")   # Keyboard not in inventory
store.display_inventory()

'''
## **5. Special Methods (Magic/Dunder Methods)**
### **Common Special Methods**
- `__str__`: String representation (`print(object)`)
- `__repr__`: Official string representation
- `__len__`: Define `len(object)`
- `__add__`: Define `object + other`
'''
### **Example**

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __len__(self):
        return self.pages
    
    def __add__(self, other):
        return Book(
            f"{self.title} & {other.title}",
            f"{self.author} and {other.author}",
            self.pages + other.pages
        )

# Usage
book1 = Book("Python Basics", "A. Smith", 300)
book2 = Book("Advanced Python", "B. Johnson", 450)

print(book1)          # Output: 'Python Basics' by A. Smith
print(len(book1))     # Output: 300
combined = book1 + book2
print(combined)       # Output: 'Python Basics & Advanced Python' by A. Smith and B. Johnson
print(len(combined))  # Output: 750
'''
## **Key Takeaways**
1. **Constructors** initialize objects with `__init__`
2. **`self`** accesses instance attributes/methods
3. **Class attributes** are shared, **instance attributes** are unique
4. **Special methods** customize object behavior
5. **Projects** should encapsulate related functionality

These concepts form the foundation of OOP in Python. Practice by extending these examples with new features like:
- Adding transaction history to BankAccount
- Implementing categories in Inventory
- Creating inheritance hierarchies (e.g., ElectronicItem inherits from InventoryItem)
'''


class A:
    name="Class A"
    def print_name(self):
        name="Class B"
        print(f"Name from {self.name}")
    print(name)
a=A()
a.print_name()