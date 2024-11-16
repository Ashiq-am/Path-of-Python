# import pandas package as pd
import pandas as pd

# Define a dictionary containing students data
data = {'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka'],
				'Age': [21, 19, 20, 18],
				'Stream': ['Math', 'Commerce', 'Arts', 'Biology'],
				'Percentage': [88, 92, 95, 70]}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data, columns = ['Name', 'Age', 'Stream', 'Percentage'])

print("Given Dataframe :\n", df)

print("\nIterating over rows using iloc function :\n")

# iterate through each row and select
# 0th and 2nd index column respectively.
for i in range(len(df)) :
    print(df.iloc[i, 0], df.iloc[i, 2])
