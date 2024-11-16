# importing pandas library
import pandas as pd

# Creating some data with strings containing special characters and numbers
data = {
	'Prices': ['12$', '-514%', '$82', '19.1%']
}

# Converting the data into dataframe by using pandas
df = pd.DataFrame(data)

# implementing the apply() method
# Using lambda expression for extracting the float values
df['Prices'] = df['Prices'].apply(
	lambda p: float(''.join(filter(str.isdigit, p)))
	if not p.isnumeric() else float(p))

# printing the dataframe
print(df)
