# importing library
import pandas as pd

# Then loading csv file
df = pd.read_csv('datasets/Fruit.csv')

# converting ;FRUIT_NAME' column into list
a = list(df['FRUIT_NAME'])

# converting list into string and then joining it with space
b = ' '.join(str(e) for e in a)

# printing result
print(b)

# converting 'PRICE' column into list
d = list(df['PRICE'])

# another way for joining used
e = '\n'.join(map(str, d))

# printing result
print(e)
