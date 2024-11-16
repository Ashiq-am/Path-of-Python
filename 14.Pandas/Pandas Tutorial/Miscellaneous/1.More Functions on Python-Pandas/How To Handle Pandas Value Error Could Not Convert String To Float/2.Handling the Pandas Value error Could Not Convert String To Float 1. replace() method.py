#importing pandas library
import pandas as pd

# Create a DataFrame with strings containing symbols
df = pd.DataFrame({'Prices': ['23-00', '56-50', '78-10', '9-05']})

# Use the `replace()` function to remove symbols
df['Prices'] = df['Prices'].replace('-', '', regex=True)


#Convert the column to float
df['Prices'] = df['Prices'].astype(float)

#Print the DataFrame
print(df)
