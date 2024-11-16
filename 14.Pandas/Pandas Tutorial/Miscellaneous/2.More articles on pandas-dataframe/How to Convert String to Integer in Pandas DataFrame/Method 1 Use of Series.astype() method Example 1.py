# import pandas library
import pandas as pd

# dictionary
Data = {'Name': ['GeeksForGeeks','Python'],
		'Unique ID': ['900','450']}

# create a dataframe object
df = pd.DataFrame(Data)

# covert string to an integer
df['Unique ID'] = df['Unique ID'].astype(int)

# show the dataframe
print (df)
print("-"*25)

# show the data types
# of each columns
print (df.dtypes)
