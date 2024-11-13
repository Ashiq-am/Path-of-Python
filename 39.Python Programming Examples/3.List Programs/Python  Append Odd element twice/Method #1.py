# Python code to create a new list from initial list
# with condition to append every odd element twice.

# List initialization
Input = [1, 2, 3, 8, 9, 11]

# Using list comprehension
Output = [elem for x in Input for elem in (x, )*(x % 2 + 1)]

# printing
print("Initial list is:'", Input)
print("New list is:", Output)
