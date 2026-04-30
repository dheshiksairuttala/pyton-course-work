#FOR LOOP WITH ELSE
#Definition:
#The else block runs only if the loop completes without encountering a break.
#Real-Time Example: Checking for Unread Notifications
#In a messaging app, we want to check if there are unread notifications. If all are read, we
#display "All caught up!"
#Code:

# 1 = Unread, 0 = Read
notifications = [0, 0, 0, 0]
for notification in notifications:
    if notification == 1:
        print("You have unread notifications!")
        break
    else:
        print("All caught up!")

#Output: All caught up!
#Explanation:
#● Since all notifications are read (0), the loop completes naturally.
#● The else block runs, confirming there are no unread messages.
#● If there was even one unread notification (1), the loop would stop, and else wouldn'trun.

#WHILE LOOP WITH ELSE
#Definition:
#Just like with for, the else runs only if the while loop completes without a break.

#Real-Time Example: OTP Verification System in an App
#Users are allowed 3 attempts to enter the correct OTP (One-Time Password). After 3 failed
#attempts, the OTP expires.
#Code:

# Simulating OTP verification
correct_otp = "7890"
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    entered_otp = input("Enter OTP: ")
    if entered_otp == correct_otp:
        print("OTP Verified Successfully!")
        break
    else:
        print("Incorrect OTP. Try again.")
        attempts += 1

else:
    print("OTP expired. Request a new one.")

#Sample Input/Output:
#Enter OTP: 1111
#Incorrect OTP. Try again.
#Enter OTP: 2222
#Incorrect OTP. Try again.
#Enter OTP: 3333
#Incorrect OTP. Try again.
#OTP expired. Request a new one.
#Explanation:
#● If OTP is not correct after 3 attempts, the else block triggers to notify that the OTP has expired.
#● If the correct OTP is entered earlier, the loop stops with break and skips else.

#break Statement in Python
#Definition:
#The break statement is used to exit a loop before it has iterated over all the items or before
#the loop condition becomes false. It is commonly used inside for or while loops when a
#specific condition is met and further looping is unnecessary or unwanted.
#Syntax:

#for item in iterable:
 #   if condition:
#        break

#or

#while condition:
#if exit_condition:
#break

#Example:

# Search for a number in a list
numbers = [1, 3, 5, 7, 9, 11]
target = 7
for num in numbers:
    if num == target:
        print("Target found:", num)
        break

#Explanation:
#The loop iterates through the list. When the target number is found, the break statement ends the loop immediately.

    #continue Statement in Python
#Definition:
#The continue statement is used to skip the rest of the code inside the current iteration of a
#loop and move to the next iteration. It does not terminate the loop entirely like break, but
#rather skips the current cycle.
#Syntax:

#for item in iterable:
#if condition:
#continue
# rest of the loop

#or

#while condition:
#if skip_condition:
#continue
# rest of the loop

#Example:

# Print odd numbers only
for num in range(1, 10):
    if num % 2 == 0:
        continue
    print(num)

#Explanation:
#The loop checks each number from 1 to 9. If a number is even, the continue statement skips printing and goes to the next iteration.

#assert Keyword in Python
#Definition:
#The assert keyword is used to perform debugging checks during development. It tests
#whether a given condition is True. If the condition is False, the program raises an
#AssertionError. It is mainly used to catch bugs by ensuring certain conditions hold true.
#Syntax:

#assert condition

#or

#assert condition, "Error message"

#Example:

#x = 10
#assert x > 0, "x must be positive"

#Explanation:
#If x is not greater than 0, the program will raise an error with the message "x must be
#positive". If the condition is true, the program continues normally.
#Use Case:
#Useful in unit testing, development phase, or validating input data. It is not recommended for
#production code, as assertions can be globally disabled with the -O (optimize) flag in Python.
