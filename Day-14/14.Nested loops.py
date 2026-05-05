#Nested Loops
#Nested loops are loops inside another loop. They are commonly used in pattern printing,
#matrix operations, and solving various algorithmic problems.
#Syntax of Nested Loops

#for i in range(outer_loop_range):
#for j in range(inner_loop_range):
# Code block to execute in the inner loop

#Understanding Nested Loops with Example

#for i in range(3): # Outer loop runs 3 times
#    for j in range(2): # Inner loop runs 2 times for each
#        outer loop
#        print(f"i={i}, j={j}")

#Output:

#i=0, j=0
#i=0, j=1
#i=1, j=0
#i=1, j=1
#i=2, j=0
#i=2, j=1

#Pattern Problems Using Nested Loops
#1. Square Pattern
#Problem Statement
#Print a square pattern of * with n rows and columns.

#Example Input

#n = 5

#Expected Output

#* * * * *
#* * * * *
#* * * * *
#* * * * *
#* * * * *

#Python Code

n = 5 # Change this for different sizes
for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()

#2. Right-Angled Triangle
#Problem Statement
#Print a right-angled triangle pattern.
#Example Input

#n = 5
#Expected Output

#*
#* *
#* * *
#* * * *
#* * * * *

#Python Code

n = 5
for i in range(n):
    for j in range(i + 1):
        print('*', end=' ')
    print()

#3. Inverted Right-Angled Triangle
#Problem Statement
#Print an inverted right-angled triangle.
#Example Input

#n = 5

#Expected Output

#* * * * *
#* * * *
#* * *
#* *
#*

#Python Code

n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()

#4. Pyramid Pattern
#Problem Statement
#Print a pyramid pattern.
#Example Input

#n = 5

#Expected Output

#*
# *
#* * *
#* * * *
#* * * * *

#Python Code

n = 5
for i in range(n):
    print(' ' * (n - i - 1) + '* ' * (i + 1))

#5. Diamond Pattern
#Problem Statement
#Print a diamond pattern.
#Example Input

#n = 5

#Expected Output

#*
#* *
#* * *
#* * * *
##* * * * *
#* * * *
#* * *
#* *
#*

#Python Code

#n = 5
# Upper part
for i in range(n):
    print(' ' * (n - i - 1) + '* ' * (i + 1))
# Lower part
for i in range(n - 2, -1, -1):
    print(' ' * (n - i - 1) + '* ' * (i + 1))

#6. Number Triangle
#Problem Statement
#Print a number triangle.

#Example Input

#n = 5

#Expected Output

#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

#Python Code

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

#7. Floyd’s Triangle
#Problem Statement
#Print Floyd’s Triangle.
#Example Input

#n = 5
#Expected Output

#1
#2 3
#4 5 6
#7 8 9 10
#11 12 13 14 15

#Python Code

n = 5
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=' ')
        num += 1
    print()

#8. Pascal’s Triangle
#Problem Statement
#Print Pascal’s Triangle.
#Example Input

#n = 5

#Expected Output

#1
#1 1
#1 2 1
#1 3 3 1
#1 4 6 4 1

#Python Code

def pascal_triangle(n):
    for i in range(n):
        print(' ' * (n - i), end=' ')
        num = 1
        for j in range(i + 1):
            print(num, end=' ')
            num = num * (i - j) // (j + 1)
        print()
pascal_triangle(5)
