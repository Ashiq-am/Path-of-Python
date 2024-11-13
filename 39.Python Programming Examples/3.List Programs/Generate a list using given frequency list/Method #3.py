# Python code to generate list containing numbers from 0 to 'n'
# having frequency of no from another list

# List initialisation
Input = [1, 4, 3, 5]

# Importing
from itertools import repeat, chain

# Using chain and enumerate
Output = list(chain.from_iterable((repeat(x, y))
				for x, y in enumerate(Input)))

# Printing output
print(Output)
