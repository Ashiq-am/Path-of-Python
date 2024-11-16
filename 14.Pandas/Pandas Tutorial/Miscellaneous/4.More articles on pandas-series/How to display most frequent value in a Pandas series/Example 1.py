# importing the module
import pandas as pd

# creating the series
series = pd.Series(['g', 'e', 'e', 'k', 's',
					'f', 'o', 'r',
					'g', 'e', 'e', 'k', 's'])
print("Printing the Original Series:")
display(series)

# counting the frequency of each element
freq = series.value_counts()
print("Printing the frequency")
display(freq)

# printing the most frequent element
print("Printing the most frequent element of series")
display(series.mode())
