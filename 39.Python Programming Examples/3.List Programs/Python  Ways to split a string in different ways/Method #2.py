# Python code to split string in substring manner

# Importing
from itertools import accumulate

# Input initialisation
Input = "Geeks_for_geeks_is_best"

# Using accumulate
Output = [*accumulate(Input.split('_'), lambda temp1, temp2 :
								'_'.join([temp1, temp2])), ]

# Printing output
print(Output)
