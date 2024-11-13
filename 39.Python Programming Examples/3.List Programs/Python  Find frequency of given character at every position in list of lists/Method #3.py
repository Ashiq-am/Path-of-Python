# Python code to find frequency of a character
# at every position of list in list of lists.

import pandas as pd

# Input list initialization
Input = [['X', 'Y', 'X'],
	['Z', 'Y', 'X'],
	['Y', 'Y', 'Y'],
	['Z', 'Z', 'X'],
	['Y', 'Z', 'X']]

# Defining character
character = 'X'

# using pandas
Output = pd.DataFrame(Input)
Output = Output.where(Output == character, 0).where(Output != character, 1)

# Printing
print("Initial list of list is :", Input)
print("Occurrence of 'X' in list is\n", Output.mean())
