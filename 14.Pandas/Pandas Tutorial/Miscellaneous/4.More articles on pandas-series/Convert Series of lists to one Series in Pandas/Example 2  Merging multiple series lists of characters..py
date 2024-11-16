# importing the module
import pandas as pd

# creating a Pandas series of lists
s = pd.Series([['g', 'e', 'e', 'k', 's'],
			['f', 'o', 'r'],
			['g', 'e', 'e', 'k', 's']])
print("Printing the Original Series of list")
print(s)

# converting series of list into one series
s = s.apply(pd.Series).stack().reset_index(drop = True)

print("\nPrinting the converted series")
print(s)
