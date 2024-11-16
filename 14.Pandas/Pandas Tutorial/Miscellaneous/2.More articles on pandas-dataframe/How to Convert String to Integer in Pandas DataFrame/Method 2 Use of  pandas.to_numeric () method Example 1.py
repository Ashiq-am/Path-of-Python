# import pandas library
import pandas as pd

# dictionary
Data = {'Name': ['GeeksForGeeks','Python'],
		'Unique ID': ['900','450']}

# create a dataframe object
df = pd.DataFrame(Data)

# convert integer to string
df['Unique ID'] = pd.to_numeric(df['Unique ID'])

# show the dataframe
print (df)
print("-"*30)

# show the data type
# of each columns
print (df.dtypes)
