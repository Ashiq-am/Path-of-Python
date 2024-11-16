# importing pandas module
import pandas as pd

# Creating pandas DataFrame
df = pd.DataFrame({"A": [1, 2, -3, 4, -5, 6],
				"B": [3, -5, -6, 7, 3, -2],
				"C": [-4, 5, 6, -7, 5, 4],
				"D": [34, 5, 32, -3, -56, -54]})

# Displaying the original DataFrame
print("Original Array : ")
print(df)

# backgroung color mapping
print("\nDataframe - Gradient color:")

# df.style.background_gradient()
df.style.background_gradient(subset='B')
