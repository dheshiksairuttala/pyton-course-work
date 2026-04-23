#Dictionary
#1. Introduction to Dictionary
#A dictionary is defined using curly braces {}, where each key is followed by a colon :, andthe key-value pairs are separated by commas.
#Syntax of a Dictionary:
#dictionary_name = {key1: value1, key2: value2, key3: value3}

#Example of a Dictionary:

student = {
"name": "Alice",
"age": 21,
"course": "Computer Science"
}
print(student)

#Output:

{'name': 'Alice', 'age': 21, 'course': 'Computer Science'}

#2. Dictionary Operations
#2.1 Accessing Values
#Dictionaries allow access to values using keys.

print(student["name"]) # Output: Alice
print(student.get("age")) # Output: 21

#Difference Between dict[key] and dict.get(key)
#● dict[key] will raise a KeyError if the key does not exist.
#● dict.get(key, default_value) will return None or the specified
#default_value if the key is not found.

print(student.get("city", "Not Available")) # Output: Not Available

#2.2 Adding and Updating Items
#You can add a new key-value pair or update an existing value by assigning a new value to a key.

student["age"] = 22 # Updating existing key
student["city"] = "New York" # Adding a new key-value pair
print(student)

#Output:

{'name': 'Alice', 'age': 22, 'course': 'Computer Science',
'city': 'New York'}

#2.3 Removing Items from a Dictionary
#There are several ways to remove elements from a dictionary.
#Using pop(key)
#Removes the specified key and returns its value.

age = student.pop("age")
print(age) # Output: 22
print(student)

#Using del
#Deletes a specific key-value pair or the entire dictionary.

del student["course"]
print(student)

#Using popitem()
#Removes and returns the last inserted key-value pair.

student.popitem()
print(student)

#Using clear()
#Removes all key-value pairs, making the dictionary empty.

student.clear()
print(student) # Output: {}

#5. Nested Dictionaries
#A dictionary can contain another dictionary as its value.

students = {
"Alice": {"age": 21, "course": "CS"},
"Bob": {"age": 22, "course": "Math"}
}
print(students["Alice"]["course"]) # Output: CS

#6. Dictionary Comprehension
#You can create dictionaries dynamically using dictionary comprehension.

squares = {x: x*x for x in range(1, 6)}
print(squares) # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#7. Real-Time Problems Using Dictionaries
#Problem 1: Count the Frequency of Words in a Sentence

sentence = "hello world hello python"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count) # Output: {'hello': 2, 'world': 1,'python': 1}

#Problem 2: Find the Student with the Highest Marks

students = {
"Alice": 85,
"Bob": 92,
"Charlie": 88
}
top_student = max(students, key=students.get)
print(top_student) # Output: Bob
