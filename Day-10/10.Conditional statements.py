#Conditional Statements
#1. if Statement
#The if statement is the most basic conditional statement. It checks if a condition is True. If it
#is, the block of code under the if statement is executed. If the condition is False, the code
#is skipped.
#Syntax:

#if condition:
# Code to execute if the condition is True

#Example: Checking Amazon Stock Availability

#amazon_stock = 20 # Number of items in stock
#if amazon_stock > 0:
 #   print("Amazon stock is available!")

#Explanation:
#● amazon_stock > 0 is the condition. It checks whether the stock is more than 0.
#● If the condition is True, it prints "Amazon stock is available!".
#● If the condition is False, nothing happens because there is no else block.

##2. if-else Statement
#The if-else statement adds an alternative path. If the if condition is True, the first block
#runs. If it is False, the else block runs.
#Syntax:

if condition:
# Code to execute if the condition is True
 else:
# Code to execute if the condition is False

#Example: Checking If Amazon Stock is Out of Stock

amazon_stock = 0 # No stock available
if amazon_stock > 0:
print("Amazon stock is available!")
else:
print("Sorry, Amazon stock is out of stock.")

#Explanation:
#● The condition amazon_stock > 0 checks if the stock is available.
#● If True, it prints "Amazon stock is available!".
#● If False, the else block executes, printing "Sorry, Amazon stock is out of stock."

#3. if-elif-else Statement
#When you have multiple conditions to check, the if-elif-else structure is used.
#● The program checks conditions one by one.
#● As soon as a condition evaluates to True, the corresponding code block runs, and
#the remaining conditions are skipped.
#● The else block is optional and only runs if none of the previous conditions are met.
#Syntax:

if condition1:
# Code if condition1 is True
elif condition2:
# Code if condition2 is True
elif condition3:
# Code if condition3 is True
else:
# Code if none of the conditions are True

#Example: Amazon Stock with Different Stock Levels

amazon_stock = 5 # Limited stock available
if amazon_stock > 20:
print("Amazon stock is fully available.")
elif amazon_stock > 0:
print("Amazon stock is low, hurry up!")
else:
print("Sorry, Amazon stock is out of stock.")

#Explanation:
#● First condition: amazon_stock > 20 checks if the stock is fully available. It's
#False, so the program moves to the next condition.
#● Second condition: amazon_stock > 0 checks if there’s limited stock. It’s True, so
#"Amazon stock is low, hurry up!" is printed.
#● The else block would run only if none of the conditions were met, meaning the stockwas 0.

#4. Nested Conditional Statements
#Nested conditional statements are when an if statement is placed inside another if or
#else block. This structure is useful when you need to check a condition only if another
#condition is already met.
#Syntax:

if condition1:
# Code if condition1 is True
if condition2:
# Code if both condition1 and condition2 are True
else:
# Code if condition1 is True but condition2 is False

else:
# Code if condition1 is False

#Example: Amazon Stock with Prime Customer Priority

amazon_stock = 3
is_prime_customer = True
if amazon_stock > 0:
print("Amazon stock is available!")
if is_prime_customer:
print("Prime customer gets priority shipping!")
else:
print("Standard shipping will apply.")

else:
print("Sorry, Amazon stock is out of stock.")

#Explanation:
#1. The outer if checks if Amazon stock is available (amazon_stock > 0).
#2. If True, it proceeds to the inner if condition that checks if the customer is a Prime
#member (is_prime_customer).
#3. Depending on the value of is_prime_customer, it prints the appropriate shippingoption.
#4. If amazon_stock <= 0, the program skips the inner condition and goes directly to
#the else block, printing "Sorry, Amazon stock is out of stock."
