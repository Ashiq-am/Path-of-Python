# Importing pandas library
import pandas as pd

# Creating 2 pandas Series
ps1 = pd.Series(['Monu', 'Sonu', 'Tonu', 'Nonu',
				'Ronu', 'Bonu'])

ps2 = pd.Series(['Sweetu', 'Tweetu', 'Nonu',
				'Micku', 'Bonu', 'Kicku'])

print("Series1:")
print(ps1)
print("\nSeries2:")
print(ps2)

# Using Bitwise NOT operator along with
# pandas.isin()
print("\nItems of ps1 not present in ps2:")
res = ps1[~ps1.isin(ps2)]
print(res)
