#Recursive Functions

#What is Recursion?
#Recursion is a programming technique where a function calls itself to solve a smaller
#instance of the same problem.
#It continues doing this until it reaches a condition where it no longer makes a recursive call.
#This is known as the base case.

#Structure of a Recursive Function
#Every recursive function has two main parts:
#1. Base Case – the condition under which the recursion stops.
#2. Recursive Case – the part where the function calls itself.

#Example 1: Factorial of a Number
#The factorial of a number n is the product of all positive integers less than or equal to n.
#Mathematical formula:

#n! = n × (n - 1) × (n - 2) × ... × 1

#Factorial using recursion:

def factorial(n):
    if n == 0 or n == 1: # Base case
        return 1
    else:
        return n * factorial(n - 1) # Recursive case
print(factorial(5)) # Output: 120

#Example 2: Fibonacci Series
#The Fibonacci sequence is:

#0, 1, 1, 2, 3, 5, 8, ...

#Where:

#F(0) = 0, F(1) = 1
#F(n) = F(n-1) + F(n-2) for n > 1

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6)) # Output: 8

#Example 3: Sum of Natural Numbers
#Calculate the sum of first n natural numbers.

def sum_natural(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural(n - 1)

print(sum_natural(5)) # Output: 15 (5 + 4 + 3 + 2 + 1)

#Pass by Value and Pass by Reference
#In Python, arguments are passed to functions by object reference. The behavior depends
#on whether the object is mutable or immutable:
#● Immutable objects (int, float, string, tuple): Behave like pass-by-value (changes
#inside the function do not affect the original object).
#● Mutable objects (list, dictionary, set, etc.): Behave like pass-by-reference
#(changes inside the function affect the original object).
#Example: Pass by Value (Immutable Objects)

def modify_value(num):
    num += 10 # This creates a new local variable
    print("Inside function:", num)

x = 5
modify_value(x)
print("Outside function:", x) # x remains unchanged

#Output:

#Inside function: 15
#Outside function: 5

#Example: Pass by Reference (Mutable Objects)

def modify_list(lst):
    lst.append(4) # Modifies the original list

numbers = [1, 2, 3]
modify_list(numbers)
print(numbers) # Output: [1, 2, 3, 4]

#How to Prevent Unintended Modifications?
#If you don’t want a function to modify the original mutable object, pass a copy:

def modify_list_copy(lst):
    lst = lst[:] # Creates a copy
    lst.append(5)
    print("Inside function:", lst)

numbers = [1, 2, 3]
modify_list_copy(numbers)
print("Outside function:", numbers) # Original list remains unchanged
