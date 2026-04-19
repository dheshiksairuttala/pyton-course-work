#Input Formatting
#1. String Input
#Use case: Entering a name, email, city, etc.
name = input("Enter your full name: ")
print(name)

#2. Integer Input
#Use case: Age, quantity, mobile number, number of items in cart.
quantity = int(input("Enter the number of items: "))
print(quantity)

#3. Float Input
#Use case: Price, temperature, discount, rating.
price = float(input("Enter the product price: "))
print(price)

#4. Input as List (Space-separated)
#Use case: List of names, marks, or product IDs.
names = input("Enter employee names (space-separated): ").split()
print(names)

#5. Input as List (Comma-separated)
#Use case: Tags, emails, product categories.
tags = input("Enter tags (comma-separated): ").split(',')
print(tags)

#6. List of Integers
#Use case: Marks, product prices, IDs.
marks = list(map(int, input("Enter marks: ").split()))
print(marks)

#7. List of Floats
#Use case: Sensor readings, weights, product prices.
weights = list(map(float, input("Enter weights: ").split()))
print(weights)

#8. Tuple Input
#Use case: Coordinates, dimensions (length, width, height).
dimensions = tuple(map(int, input("Enter length, width, height: ").split()))
print(dimensions)

#9. Set Input
#Use case: Selected image IDs where duplicates must be removed (e.g., in a photo-sharingapp).
selected_ids = set(map(int, input("Enter selected image IDs :").split()))
print(selected_ids)

#10. Dictionary Input using eval()
#Use case: When entering structured data like configuration settings or user profiles.
profile = eval(input("Enter user profile as a dictionary: "))
print(profile)

#11. Multiple Inputs with Unpacking
#Use case: Login form or payment details.
username, password = input("Enter username and password: ").split()
print("Username:", username)
print("Password:", password)



#Output Formatting
#What is print()?
#The print() function in Python outputs text, numbers, or any other data type to the console. It's one of the first functions every Python programmer learns.
#Basic Syntax:
print(object, ..., sep=' ', end='\n', file=sys.stdout,
flush=False)

#Basic Examples of print()
#a) Printing Text

print("Hello, World!")

#b) Printing Multiple Items

name = "Alice"
age = 25
print("Name:", name, "Age:", age)

#Output: Name: Alice Age: 25

#c) Using sep to Change the Separator

print("2024", "02", "07", sep="-")

#Output: 2024-02-07
#Instead of spaces, hyphens (-) are used as separators.

#d) Using end to Control Line Endings

print("Hello,", end=" ")
print("World!")

#Output: Hello, World!
#Here, end=" " prevents the default new line, and the second print() continues on the same line.

#Printing Special Characters
#● New Line (\n):

print("Line 1\nLine 2")

#Output:
#Line 1
#Line 2

#● Tab (\t):

print("Name:\tAlice")

#● Output: Name: Alice


#Output Formatting
#1️⃣Using Commas (Simple Print Method)
#This is the most basic way to print multiple items. When you separate items with commas in
#the print() function, Python adds a space between them automatically.

name = "Alice"
age = 25
score = 95.5
# Using Commas
print("Name:", name, "Age:", age, "Score:", score)

#Output: Name: Alice Age: 25 Score: 95.5

#2️⃣Using Modulo Operator (% Formatting)
#This is an older method, similar to C-style formatting.
#You use % followed by format specifiers like %s (string), %d (integer), %f (float), etc.

name = "Bob"
age = 30
score = 88.75
# Using Modulo Operator
print("Name: %s | Age: %d | Score: %.2f" % (name, age, score))

#● %s → String
#● %d → Integer
#● %.2f → Float with 2 decimal places
#Output: Name: Bob | Age: 30 | Score: 88.75

#3️⃣Using f-strings (Formatted String Literals) — Python 3.6+
#This is the most modern and recommended method.
#Add an f before the string and use curly braces {} to insert variables directly.

name = "Charlie"
age = 28
score = 92.389
# Using f-strings
print(f"Name: {name} | Age: {age} | Score: {score:.2f}")

#● {score:.2f} → Displays the score with 2 decimal places.
#Output: Name: Charlie | Age: 28 | Score: 92.39


#4️⃣Using str.format() Method
#This method works in both Python 2 and 3.
#You use {} as placeholders and call .format() with the variables you want to insert.

name = "Diana"
age = 22
score = 89.456
# Using str.format()
print("Name: {} | Age: {} | Score: {:.1f}".format(name, age,
score))

#● {} → Placeholder for variables.
#● {:.1f} → Formats the score with 1 decimal place.
#Output: Name: Diana | Age: 22 | Score: 89.5
