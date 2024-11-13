# Python code to generate list containing numbers from 0 to 'n'
# having frequency of no from another list

# List initialisation
Input = [1, 4, 3, 5]

# Using enumerate and list comprehension
Output = [no for no, rep in enumerate(Input)
					for elem in range(rep)]

# Printing output
print(Output)
