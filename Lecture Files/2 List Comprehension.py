# List Comprehension

# ----------------------------------------------------
# region Introduction to List Comprehension
# ----------------------------------------------------
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Basic syntax: [expression for item in iterable if condition]

# Example: Even Numbers
# As standard for loop
numbers = range(1, 11)  # Example input list
even_numbers = []  # Initialize an empty list for even numbers

for number in numbers:  # Iterate over each number in the list
    if number % 2 == 0:  # Check if the number is even
        even_numbers.append(number)  # Append even number to the list

print("Even numbers:", even_numbers)  # Output the list of even numbers

# As list comprehension
numbers = range(1, 11)
even_numbers = [number for number in numbers if number % 2 == 0]
print("Even numbers:", even_numbers)

# TODO: Activity 1 - Create a List of Even Numbers
# First, create a list of numbers from 1 to 5.
# Next, use list comprehension to create a new list of those numbers squared.
# Your code here:


# endregion

# ----------------------------------------------------
# region Benefits of Using List Comprehension
# ----------------------------------------------------
# List comprehension can make code more concise and readable, especially for simple operations and transformations.

# Example: Filtering a List
inventory = ["hammer", "screwdriver", "wrench", "pliers"]
tools_with_r = [tool for tool in inventory if 'r' in tool]
print("Tools containing 'r':", tools_with_r)

# TODO: Activity 2 - Filter List for Specific Length
# First, create a list of materials: "steel", "aluminum", "copper", "plastic".
# Next, use list comprehension to create a list of materials with more than 6 characters.
# Your code here:

# endregion

# ----------------------------------------------------
# region Advanced List Comprehension
# ----------------------------------------------------
# Advanced list comprehension can include nested conditions, multiple for loops, and complex expressions.

# Example: Flattening a Matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Flattened matrix:", flattened)

# TODO: Activity 4 - List Comprehension with Nested Conditions
# First, create a nested list (matrix) with 3 rows, each containing numbers from 1 to 3.
# Next, use list comprehension to create a list of these numbers squared, but only if the number is even.
# Your code here:

# endregion

# ----------------------------------------------------
# region Using Multiple For Clauses
# ----------------------------------------------------
# You can use multiple for clauses in a list comprehension to simulate nested loops.

# Example: Generating Coordinate Pairs
x_range = [1, 2, 3]
y_range = [4, 5]
coordinates = [(x, y) for x in x_range for y in y_range]
print("Coordinate pairs:", coordinates)

# TODO: Activity 5 - Generate Multiplication Results List
# First, create two ranges: one for the multipliers (1-3) and one for the multiplicands (1-2).
# Next, use list comprehension to create a list of the results of multiplying each pair of numbers from the multipliers and multiplicands.
# Your code here:

# endregion
