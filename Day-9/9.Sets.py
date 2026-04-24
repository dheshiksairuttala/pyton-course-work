#Sets
#1. Introduction to Sets
#● A set is an unordered, mutable collection of unique elements.
#● Sets automatically remove duplicate elements.
#● Sets are similar to mathematical sets and support operations like union, intersection,and difference.
#● They are useful for storing unique elements and performing fast membership tests.Set Creation Syntax:

# Creating a set with unique elements
my_set = {1, 2, 3, 4}
# Creating an empty set (use set() function, not {})
empty_set = set()
# Set with duplicate elements (duplicates are removed automatically)
set_with_duplicates = {1, 2, 2, 3, 4}
print(set_with_duplicates) # Output: {1, 2, 3, 4}

#2. Set Properties
#● Unique Elements: Duplicate elements are not allowed.
#● Mutable: Sets can be modified (elements can be added or removed).
#● Immutable Elements Only: Elements must be hashable (mutable types like listscannot be elements).
#Example of an invalid set (due to mutable elements):

# This will raise a TypeError
invalid_set = {[1, 2], 3} # Lists are mutable and cannot be added to a set

#3. Operations on Sets
#Python provides several set operations that mimic mathematical set theory.
#a. Membership Testing
#● Check if an element is present using the in or not in keywords.
#● Example:

my_set = {1, 2, 3, 4}
print(3 in my_set) # Output: True
print(5 not in my_set) # Output: True

#b. Union (| or union() method)
#● Combines elements from two sets (removes duplicates).
#● Syntax: set1 | set2 or set1.union(set2)
#● Example:

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 | set2 # Output: {1, 2, 3, 4, 5}

#c. Intersection (& or intersection() method)
#● Returns common elements between two sets.
#● Syntax: set1 & set2 or set1.intersection(set2)
#● Example:

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 & set2 # Output: {3}

#d. Difference (- or difference() method)
#● Returns elements in the first set but not in the second set.
#● Syntax: set1 - set2 or set1.difference(set2)
#● Example:
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 - set2 # Output: {1, 2}

#e. Symmetric Difference (^ or symmetric_difference() method)
#● Returns elements in either set1 or set2 but not both.
#● Syntax: set1 ^ set2 or set1.symmetric_difference(set2)
#● Example:

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 ^ set2 # Output: {1, 2, 4, 5}

#f. Subset (<= or issubset() method)
#● Checks if all elements of one set are present in another.
#● Syntax: set1 <= set2 or set1.issubset(set2)
#● Example:

set1 = {1, 2}
set2 = {1, 2, 3}
print(set1 <= set2) # Output: True

#g. Superset (>= or issuperset() method)
#● Checks if one set contains all elements of another.
#● Syntax: set1 >= set2 or set1.issuperset(set2)
#● Example:

set1 = {1, 2, 3}
set2 = {1, 2}
print(set1 >= set2) # Output: True

#h. Disjoint Sets (isdisjoint() method)
#● Returns True if two sets have no common elements.
#● Example:

set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2)) # Output: True

#6. Immutability and Frozensets
#● Frozensets are immutable versions of sets.
#● Once a frozenset is created, its elements cannot be changed.
#● Useful for creating hashable, immutable collections.
#Example:

# Creating a frozenset
frozen = frozenset([1, 2, 3])
print(frozen)
# Frozenset is immutable
# The following will raise an error
# frozen.add(4)
