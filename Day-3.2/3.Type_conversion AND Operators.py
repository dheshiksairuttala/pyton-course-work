#Type Conversion (Type Casting)
#Type conversion in Python refers to converting the value of one data type to another usingbuilt-in functions such as int(), float(), str(), bool(), list(), tuple(), set(),and dict().
#1. Converting from int
int_a = 2

#2. Converting from float
float_n = 3.1

#3.Converting from str
string_c = 'power'

#4. Converting from list
list_d = [1, 2, 3, 4]

#5. Converting from tuple
tuple_f = (1, 2, 3, 4)

#6. Converting from set
set_e = {3, 4, 5, 6}

#7. Converting from dict
dict_g = {1: 1, 2: 4, 3: 9}

#8. Converting from bool
boolean = False

#9. Dictionary Conversion
d = [('name', 'teja'), ('batch', '22'), ('subject', 'python')]
dict(d)
# Output: {'name': 'teja', 'batch': '22', 'subject': 'python'}



#Python Operators
#1. Arithmetic Operators
a = 10
b = 3
print(a + b) # Output: 13
print(a - b) # Output: 7
print(a * b) # Output: 30
print(a / b) # Output: 3.3333
print(a // b) # Output: 3
print(a % b) # Output: 1
print(a ** b) # Output: 1000

#2. Comparison Operators
x = 10
y = 5
print(x == y) # Output: False
print(x != y) # Output: True
print(x > y) # Output: True
print(x < y) # Output: False
print(x >= 10) # Output: True
print(y <= 5) # Output: True

#3. Assignment Operators
x = 10
x += 5 # x = x + 5 → 15
x *= 2 # x = x * 2 → 30
x -= 10 # x = x - 10 → 20
print(x) # Output: 20

#4. Logical Operators (Using Logic Gates)
x = 10
y = 20
print(x > 5 and y < 30) # Output: True (Both conditions areTrue)
print(x > 15 or y < 30) # Output: True (At least onecondition is True)
print(not (x > 5)) # Output: False (Reverses the Truecondition)

#5. Membership Operators
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits) # Output: True
print("grape" not in fruits) # Output: True

#6. Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b) # Output: True (Both refer to the sameobject)
print(a is c) # Output: False (Different objects with thesame content)
print(a is not c) # Output: True

#7. Bitwise Operators (With Binary Representation)
x = 5 # Binary: 0101
y = 3 # Binary: 0011
print(x & y) # Output: 1 (Binary: 0001 → AND operation)
print(x | y) # Output: 7 (Binary: 0111 → OR operation)
print(x ^ y) # Output: 6 (Binary: 0110 → XOR operation)
print(~x) # Output: -6 (Binary: Inverts bits of 5)
print(x << 1) # Output: 10 (Binary: 1010 → Shifts left by 1)
print(x >> 1) # Output: 2 (Binary: 0010 → Shifts right by 1)
