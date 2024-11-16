#importing pandas library
import pandas as pd

#Creating some random data with strings containing special characters
data = {
	'Prices': ['$12', '#8', '12%', '1.21']
}

#Converting the data into dataframe by using pandas
df = pd.DataFrame(data)

#Use the `to_numeric()` function to convert the column to float
df['Prices'] = pd.to_numeric(df['Prices'], errors='coerce')

#print the data frame
print(df)
