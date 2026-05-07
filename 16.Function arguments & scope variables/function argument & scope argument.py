#Function Arguments
#Python allows different types of function arguments:
#1. Positional Arguments
#Arguments are passed in the order they are defined in the function.

def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")
greet("Alice", 25)

#2. Keyword Arguments
#Arguments are specified with the parameter names.

#greet(age=25, name="Alice")

#3. Default Arguments
#Provides default values if no argument is provided.

def greet(name, age=18):
    print(f"Hello {name}, you are {age} years old.")

greet("Bob") # Uses default age=18

#4. Variable-Length Arguments
#*args (Arbitrary Positional Arguments)
#Used to pass a variable number of arguments.

def add(*numbers):
    return sum(numbers)

print(add(1, 2, 3, 4, 5))

#**kwargs (Arbitrary Keyword Arguments)
#Used to pass multiple keyword arguments.

def user_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

user_info(name="Alice", age=25, city="New York")

#1. Local Scope
#Variables declared inside a function are local to that function.

def greet():
    message = "Hello"
    print(message)
greet()
# print(message) # Error: message is not defined outside

#● message is a local variable and only accessible inside greet().

#2. Global Scope
#A variable declared outside all functions is global and can be accessed inside functions
#(but not modified unless declared global).

x = 10 # Global variable

def show():
    print(x) # Accessing global variable
show()

#● You can read global variables inside functions, but to modify them, use the global
#keyword:

x = 10

def update():
    global x
    x = 20
update()
print(x) # Output: 20

#3. Enclosing Scope (Nonlocal Scope)
#This occurs in nested functions. The variable in the outer (enclosing) function is accessible
#to the inner function, but not modifiable unless nonlocal is used.
def outer():
    msg = "Hi"

    def inner():
        print(msg) # Enclosing scope variable
        inner()
    outer()

#To modify the enclosing variable, use nonlocal:

def outer():
    msg = "Hi"

    def inner():
        nonlocal msg
        msg = "Hello"
    inner()
    print(msg) # Output: Hello
outer()

#4. Built-in Scope
#Names like len, print, range, etc., come from Python’s built-in scope and are available
#everywhere.

print(len("Python")) # len is a built-in function

#Avoid using built-in names as variable names:

#len = 5 # Overrides the built-in len
#print(len("test")) # Error

#LEGB Rule Summary
#When you use a variable, Python searches for it in the following order:
#1. L – Local scope (inside the current function)
#2. E – Enclosing scope (functions inside functions)
#3. G – Global scope (module-level)
#4. B – Built-in scope (Python’s built-in names)

#Example of LEGB Rule

x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x) # Looks for local, enclosing, global,built-in
    inner()
outer()

#Output: local

#Shadowing Variables
#If you declare a variable in a local scope with the same name as a global one, it shadows
#the global variable within that scope.

x = 100

def func():
    x = 50 # Local variable shadows global x
    print(x)
func()
print(x) # Global x remains unaffected
