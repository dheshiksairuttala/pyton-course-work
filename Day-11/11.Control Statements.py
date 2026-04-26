#Control Statements
#FOR LOOP
#Definition:
#A for loop is used to iterate over items like lists, strings, or ranges.
#Real-Time Example: Checking Daily App Usage (Streaks Feature)
#Imagine a fitness app tracking if users completed their daily workouts over a week.
#● 1 = Workout done
#● 0 = Workout missed
#We want to find the longest streak of consecutive workout days.
#Code:

# User's workout record over a week
workout_log = [1, 1, 1, 0, 1, 1, 0]
current_streak = 0
longest_streak = 0
for day in workout_log:
    if day == 1:
       current_streak += 1
       if current_streak > longest_streak:
           longest_streak = current_streak

    else:
        current_streak = 0 # Streak breaks
print("Longest workout streak:", longest_streak)

#Output: Longest workout streak: 3

#WHILE LOOP
#Definition:
#A while loop repeats a block of code as long as a condition is True.
#Real-Time Example: Limiting Login Attempts in a Mobile App
#In a banking app, users can only attempt to log in 3 times before their account is
#temporarily locked.
#Code:

# Simulating incorrect login attempts
correct_pin = "1234"
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    entered_pin = input("Enter your PIN: ")
    if entered_pin == correct_pin:
        print("Login successful!")
        break
    else:
        print("Incorrect PIN. Try again.")
        attempts += 1

else:
    print("Account locked due to too many failed attempts.")

#Sample Input/Output:
#Enter your PIN: 1111
#Incorrect PIN. Try again.
#Enter your PIN: 2222
#Incorrect PIN. Try again.
#Enter your PIN: 3333
#Incorrect PIN. Try again.
#Account locked due to too many failed attempts.

#Explanation:
#● The loop allows a maximum of 3 attempts.
#● If the correct PIN isn’t entered in 3 tries, the account gets locked.
#● The else block executes only if the loop ends without a successful login.
