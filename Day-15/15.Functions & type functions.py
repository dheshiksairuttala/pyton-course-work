#Functions

#Definition of Functions
#A function in Python is a reusable block of code that performs a specific task. It helps in
#breaking down large programs into smaller, manageable parts. Functions improve code
#reusability, readability, and modularity.
#Syntax of a Function in Python:

#def function_name(parameters):
#"""Docstring explaining the function"""
# Function body
#return value # Optional

#Example:

def greet(name):
    """This function returns a greeting message."""
    return f"Hello, {name}!"
print(greet("Alice")) # Output: Hello, Alice!

#Features of Functions in Python
#1. Code Reusability - Write once, use multiple times.
#2. Modularity - Divide code into logical sections.
#3. Maintainability - Easier to debug and modify.
#5. Encapsulation - Hides implementation details from users.
#6. Parameterization - Functions accept arguments to perform operations dynamically.
#7. Return Values - Functions can return values for further use.


#Types of Functions
#Python provides different types of functions based on their usage and definition:
#1. Built-in Functions
#These are pre-defined functions available in Python that perform common operations without
#requiring user implementation.
#Common Built-in Functions:
#● print(): Outputs text to the console.
#● abs(): Returns the absolute value of a number.
#● max(): Returns the largest value from a set of numbers.
#● sorted(): Returns a sorted list.

#Examples:

print(len("Hello")) # Output: 5
print(abs(-10)) # Output: 10
print(max(1, 5, 3)) # Output: 5
print(sorted([3, 1, 4, 2])) # Output: [1, 2, 3, 4]

#2. User-Defined Functions
#These are functions created by the user to perform specific tasks. They allow programmers
#to implement custom logic for their applications.
#Example:

def add(a, b):
    """This function adds two numbers."""
    return a + b

print(add(5, 10)) # Output: 15
