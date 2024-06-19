# Introduction to Lists

# ----------------------------------------------------
# region Definition and Characteristics of Lists
# ----------------------------------------------------
# Lists in Python are ordered collections of items that can be of any type.
# Lists are defined by enclosing values in square brackets, separated by commas.

# Example: Creating a List
inventory_items = ["pumps", "valves", "compressors"]
print(inventory_items)

# TODO: Activity 1 - Create Your Own List
# First, create a list named `tools` containing at least three different types of tools.
# Next, print the list.
# Your code here:

# endregion

# ----------------------------------------------------
# region Accessing List Elements
# ----------------------------------------------------
# You can access elements in a list by indexing, starting from 0 for the first element.
# Slicing allows you to obtain a sublist by specifying a range of indices.

# Example: Indexing and Slicing
print(inventory_items[0])  # Accesses the first element
print(inventory_items[-1])  # Accesses the last element
print(inventory_items[1:3])  # Slices the list to include elements at index 1 and 2

# TODO: Activity 2 - Access Elements in Your List
# First, print the first tool in your `tools` list.
# Next, print the last two tools in the list using slicing.
# Your code here:

# endregion

# ----------------------------------------------------
# region Adding and Removing Elements
# ----------------------------------------------------
# Elements can be added to a list using append() and insert() methods.
# Elements can be removed using remove(), pop(), and the del statement.

# Example: Modifying a List
inventory_items.append("tubes")  # Adds an item to the end
inventory_items.insert(1, "gaskets")  # Inserts an item at index 1
inventory_items.pop()  # Removes the last item
print(inventory_items)

# TODO: Activity 3 - Modify Your Tools List
# First, add a new tool to the end of your `tools` list.
# Next, remove the first tool from the list.
# Your code here:

# endregion

# ----------------------------------------------------
# region List Concatenation and Replication
# ----------------------------------------------------
# Lists can be concatenated using the + operator, and replicated using the * operator.

# Example: Concatenating and Replicating Lists
more_items = ["bearings", "motors"]
full_inventory = inventory_items + more_items
print(full_inventory)
replicated_items = more_items * 2
print(replicated_items)

# TODO: Activity 4 - Concatenate and Replicate Your List
# First, create a new list named `more_tools` with at least two tools.
# Next, concatenate `tools` and `more_tools` and print the result.
# Then, replicate `more_tools` by 2 and print the result.
# Your code here:

# endregion

# ----------------------------------------------------
# region Iterating Over Lists
# ----------------------------------------------------
# You can iterate over the elements of a list using a for loop to perform operations on each element.

# Example: Iterating Over a List
for item in inventory_items:
    print(f"Inventory item: {item}")

# TODO: Activity 4 - Check Tools
# First, iterate over `tools` and print each tool with a message indicating it is in stock.
# Your code here:

# endregion

# ----------------------------------------------------
# region List Length and Existence Check
# ----------------------------------------------------
# Use len() to get the number of items in a list. Use the in keyword to check if an item exists in a list.

# Example: Checking Length and Existence
print(len(inventory_items))  # Prints the number of items in inventory
print("helmet" in inventory_items)  # Checks if "helmet" is in inventory

# TODO: Activity 5 - Drill Check
# First, print the total number of items in `tools`.
# Next, check if "drill" is in the tools list and print a corresponding message.
# Your code here:

# endregion
