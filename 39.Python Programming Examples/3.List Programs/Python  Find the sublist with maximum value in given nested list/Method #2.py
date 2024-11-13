# Python code to find maximum value
# in second column of list of list

# Importing
import operator

# Input list initialization
Input = [['Paras', 90], ['Jain', 32], ['Geeks', 120],
						['for', 338], ['Labs', 532]]
# Using itemgetter
Output = max(Input, key = operator.itemgetter(1))

# Printing output
print("Input List is :", Input)
print("Output list is : ", Output)
