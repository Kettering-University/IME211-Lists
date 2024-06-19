# Manipulating Lists

# ----------------------------------------------------
# region Sorting Lists
# ----------------------------------------------------
# Lists can be sorted in place using the sort() method, or a new sorted list can be created with the sorted() function.

# Example: Sorting a List of Product Codes
product_codes = ['P234', 'P123', 'P456']
product_codes.sort()
print("Sorted product codes:", product_codes)

sorted_codes = sorted(['P678', 'P789', 'P567'], reverse=True)
print("Reverse sorted product codes:", sorted_codes)

# TODO: Activity 1 - Sort Equipment List
# First, create a list named `equipment` with at least five different pieces of equipment.
# Next, use the sort() method to sort `equipment` in reverse alphabetical order and print the list.
# Your code here:

# endregion

# ----------------------------------------------------
# region Reversing Lists
# ----------------------------------------------------
# The reverse() method reverses the elements of the list in place.

# Example: Reversing a List of Numbers
numbers = [101, 103, 102, 104]
numbers.reverse()
print("Reversed numbers:", numbers)

# TODO: Activity 2 - Reverse Inventory List
# First, create a list named `inventory` with at least four different inventory items.
# Next, use the reverse() method to reverse the order of `inventory` and print the list.
# Your code here:

# endregion

# ----------------------------------------------------
# region Nesting Lists
# ----------------------------------------------------
# Lists can contain other lists as elements, allowing for the creation of nested data structures.

# Example: Nested List of Warehouse Locations
warehouse_locations = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
print("Warehouse location A2:", warehouse_locations[0][1])

# TODO: Activity 3 - Create Nested List for Project Teams
# First, create a nested list named `project_teams` where each sub-list contains the names of team members for different projects.
# Next, print the names of team members for the first project.
# Your code here:

# endregion

# ----------------------------------------------------
# region Common List Methods
# ----------------------------------------------------
# The index() method returns the index of the first occurrence of an element. The count() method returns the number of times an element appears.

# Example: Using index() and count()
materials = ['Steel', 'Aluminum', 'Copper', 'Steel', 'Copper']
print("Index of 'Copper':", materials.index('Copper'))
print("'Steel' count:", materials.count('Steel'))

# TODO: Activity 4 - Find and Count Materials
# First, add another 'Aluminum' to the `materials` list.
# Next, print the index of the first occurrence of 'Aluminum' and count how many times 'Aluminum' appears in the list.
# Your code here:

# endregion

# ----------------------------------------------------
# region Copying Lists
# ----------------------------------------------------
# Lists can be copied using the copy() method or the slicing syntax [:] to create a shallow copy.

# Example: Copying a List of Tools
tools = ['Screwdriver', 'Hammer', 'Wrench']
tools_copy = tools.copy()
tools_slice_copy = tools[:]
print("Original tools:", tools)
print("Copied tools:", tools_copy)
print("Sliced copied tools:", tools_slice_copy)

tools_reference = tools  # This does not create a copy, instead it creates another reference to the same object

# TODO: Activity 5 - Duplicate and Modify Tool List
# First, create a copy of the `tools` list named `new_tools` using the copy() method.
# Next, add 'Drill' to `new_tools` and print both lists to show they are independent.
# Your code here:

# endregion
