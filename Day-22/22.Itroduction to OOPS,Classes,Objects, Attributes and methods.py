#Classes
#- A class is a blueprint for creating objects.
#- It defines the attributes (data) and methods (functions) that the objects will have.
#Example: E-commerce Product Class

# Step 1: Define a class
class Product:
# Attributes (data)
#name = "Laptop"
#price = 50000
#quantity = 10
# Methods (functions)
#def display_info(self):
#   print(f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}")

#Objects
#- An object is an instance of a class.
#- You can create multiple objects from a single class.
#Example: Creating Objects

# Step 2: Create objects of the Product class
#product1 = Product() # Object 1
#product2 = Product() # Object 2
# Access attributes and methods
#product1.display_info() # Output: Product: Laptop, Price: 50000, Quantity: 10
#product2.display_info() # Output: Product: Laptop, Price: 50000, Quantity: 10

#Attributes
#Attributes are variables that store the state of an object.
#Example: Modifying Attributes

# Step 3: Modify attributes
#product1.name = "Smartphone"
#product1.price = 30000
#product1.quantity = 5
#product1.display_info() # Output: Product: Smartphone, Price: 30000, Quantity: 5

#1. Types of Attributes
#They can be categorized as follows:
#(a) Instance Attributes
#● Defined inside the __init__ constructor using self.
#● Unique for each instance of the class.

#Example:
class Product:
    def __init__(self, name, price, quantity):
        self.name = name # Instance Attribute
        self.price = price
        self.quantity = quantity
# Creating two different product instances
p1 = Product("Laptop", 50000, 10)
p2 = Product("Phone", 20000, 5)
print(p1.name) # Laptop
print(p2.name) # Phone

#(b) Class Attributes
#● Shared among all instances of the class.
#● Defined outside __init__ and accessed using ClassName.attribute.
#Example:
class Product:
    discount = 10 # Class Attribute
def __init__(self, name, price):
    self.name = name
    self.price = price
# Accessing class attribute
print(Product.discount) # 10

#Methods
#- Methods are functions that belong to a class.
#- They define the behavior of the object

#Example: Adding a Method

# Step 4: Add a method to calculate total price
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        def display_info(self):
            print(f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}")
        def calculate_total_price(self):
            return self.price * self.quantity
# Create an object
product1 = Product("Tablet", 20000, 3)
print("Total Price:", product1.calculate_total_price()) # Output: Total Price: 60000

#Types of Methods
#There are three types:
#(a) Instance Methods
#● Work with instance attributes (self).
#● Can modify instance-specific data.
#Example:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        def apply_discount(self, discount):
            self.price -= self.price * (discount / 100)
p1 = Product("Laptop", 50000)
p1.apply_discount(10)
print(p1.price) # 45000

#(b) Class Methods
#● Use @classmethod decorator.
#● Work with class attributes using cls.
#Example:
class Product:
    discount = 10 # Class Attribute
    @classmethod
    def set_discount(cls, new_discount):
        cls.discount = new_discount # Modifies class attribute
Product.set_discount(15)
print(Product.discount) # 15

#(c) Static Methods
#● Use @staticmethod decorator.
#● Independent of both instance and class attributes.
#● Used for utility functions.
#Example:
class Product:
    @staticmethod
    def is_expensive(price):
        return price > 30000
print(Product.is_expensive(50000)) # True
print(Product.is_expensive(20000)) # False

#Real-world example of an E-commerce Product class with attributes and methods:

class Product:
    discount = 5 # Class Attribute (default discount for all products)
    def __init__(self, name, price, quantity):
        self.name = name # Instance Attribute
        self.price = price
        self.quantity = quantity
    def apply_discount(self):
        """Instance Method: Applies discount to price"""
        self.price -= self.price * (self.discount / 100)
    @classmethod
    def update_discount(cls, new_discount):
        """Class Method: Updates discount for all products"""
        cls.discount = new_discount
    @staticmethod
    def is_available(quantity):
        """Static Method: Checks if product is available"""
        return quantity > 0
# Creating product instances
p1 = Product("Laptop", 50000, 10)
p2 = Product("Phone", 20000, 5)
# Applying discount
p1.apply_discount()
print(p1.price) # 47500 (5% discount applied)
# Updating discount for all products
Product.update_discount(10)
p2.apply_discount()
print(p2.price) # 18000 (10% discount applied)
# Checking product availability
print(Product.is_available(p1.quantity)) # True
