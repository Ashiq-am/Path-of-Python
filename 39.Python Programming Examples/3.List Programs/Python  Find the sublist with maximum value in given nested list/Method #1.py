# Python code to find maximum value
# in second column of list of list

# Input list initialization
Input = [['Paras', 90], ['Jain', 32], ['Geeks', 120],
						['for', 338], ['Labs', 532]]
# Using lambda
Output = max(Input, key = lambda x: x[1])

# printing output
print("Input List is :", Input)
print("Output list is : ", Output)
