import pandas as pd
# Example DataFrame
data = {'Category': ['Fruits', 'Vegetables', 'Dairy'],
		'Contains': ['Apple,Orange,Banana', 'Carrot,Potato,Tomato,Cucumber', 'Milk,Cheese,Yogurt']}
df = pd.DataFrame(data)

# Split the 'Items_string' column by commas and create a new column 'Items_list'
df['Contains_list'] = df['Contains'].str.split(',')

# Display the DataFrame
print(df)
