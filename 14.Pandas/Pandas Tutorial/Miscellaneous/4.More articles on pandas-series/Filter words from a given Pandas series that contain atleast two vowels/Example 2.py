import pandas as pd
from collections import Counter

# creating a series of words
series = pd.Series(['Apple', 'Banana', 'Cherry',
					'Plum', 'Orange', 'Fig', 'Melon'])

print("Original Series:")
print(series)
print("\nWords containing atleast 2 vowels")

# mapping through the series and checking
# if count of vowels is >=2
result = series[series.str.count('(?i)[aeiou]') >=2]

print(series[result])
