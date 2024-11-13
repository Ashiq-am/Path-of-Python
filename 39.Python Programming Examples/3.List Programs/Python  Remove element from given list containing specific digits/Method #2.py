# Python code to remove all those elements from list
# which contains certain digits

# Input List Initialisation
Input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 13, 15, 16]

# Numbers to delete
no_delete = ['2', '3', '4', '0']

# using list comprehension and any()
Output = [a for a in Input if not
		any(b in no_delete for b in str(a))]

# Printing Output
print("Intial list is :", Input)
print("Delete list :", no_delete)
print("List after removing elements is :", Output)
