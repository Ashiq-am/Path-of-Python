# importing the module
import pandas as pd

# creating a Pandas series of lists
s = pd.Series([[2, 4, 6, 8],
			[1, 3, 5, 7],
			[2, 3, 5, 7]])
print("Printing the Original Series of list")
print(s)

# converting series of list into one series
s = s.apply(pd.Series).stack().reset_index(drop = True)

print("\nPrinting the converted series")
print(s)
