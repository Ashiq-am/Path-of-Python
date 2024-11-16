import pandas as pd
s = pd.read_csv("stock.csv", squeeze = True)

# adding 5 to each value
new = s.apply(lambda num : num + 5)

# printing first 5 elements of old and new series
print(s.head(), '\n', new.head())

# printing last 5 elements of old and new series
print('\n\n', s.tail(), '\n', new.tail())
