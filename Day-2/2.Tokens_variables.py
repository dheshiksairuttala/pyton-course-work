#Tokens in Python
#1. Keywords – Reserved words in Python (e.g., if, else, while, for, def).
#2. Identifiers – Names given to variables, functions, and classes.
#3. Literals – Constant values assigned to variables (e.g., 10, "Hello", 3.14).
#4. Operators – Symbols that perform operations (e.g., +, -, *, /).
#5. Punctuators – Symbols like (), {}, [], ,, :,. used for syntax structuring.
# This program calculates the area of a rectangle
length = 10
width = 5
area = length * width
if area > 30:
    print("Large area")
else:
    print("Small area")
#Statements and Identifiers
x = 10 # Assignment statement
print(x) # Function call statement
#What is an Identifier?
age = 25 # 'age' is an identifier for the variable
def greet(): # 'greet' is an identifier for a function
#Examples of Valid and Invalid Identifiers
 age = 25 # 'age' is an identifier (valid)
_name = "John" # '_name' is a valid identifier
score1 = 88 # valid: letters + digits

# Invalid examples (will cause errors if uncommented)
# 1age = 30 # Invalid: starts with a digit
# def = 5 # Invalid: 'def' is a Python keyword
#Comments in Python
# This is a single-line comment
x = 10 # This is also a comment
#What Are Keywords?
#Keywords are reserved words in Python that have special meanings and purposes.
#They are part of the Python syntax and cannot be used as identifiers (variable, function, or class names).
import keyword

print(keyword.kwlist) # List of all keywords
print(len(keyword.kwlist)) # Total number of keywords
#What is a Variable?
#A variable is a named memory location used to store data in a Python program.
#It acts as a label for a value that you want to use or modify during program execution.
#Basic Variable Assignment
product_name = "Laptop"
price = 45000
in_stock = True
print(product_name, price, in_stock)
#Multiple Assignment
#Python allows assigning values to multiple variables in a single line.
a, b, c = 10, 20, 30
print(a, b, c) # Output: 10 20 30
#You can also assign the same value to multiple variables:
x = y = z = 100
print(x, y, z) # Output: 100 100 100
#Reassignment
#A variable’s value can be updated or reassigned at any point.
x = 5
x = 10
print(x) # Output: 10
#Swapping Variables
#Python allows swapping values of two variables without using a temporary variable:
a, b = 5, 10
a, b = b, a
print(a, b) # Output: 10 5
#Deleting Variables
#Use the del keyword to delete a variable:
x = 100
del x
# print(x) # Raises: NameError: name 'x' is not defined
