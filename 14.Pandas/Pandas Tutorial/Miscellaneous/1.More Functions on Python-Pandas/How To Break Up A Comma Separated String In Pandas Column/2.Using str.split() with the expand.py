import pandas as pd

# Example DataFrame
data = {'Category': ['Fruits', 'Vegetables', 'Dairy'],
		'Contains': ['Apple,Orange,Banana', 'Carrot,Potato,Tomato,Cucumber', 'Milk,Cheese,Yogurt']}
df = pd.DataFrame(data)

# Split the 'Contains' column by commas and expand it into separate columns
df[['Item1', 'Item2', 'Item3', 'Item4']] = df['Contains'].str.split(',', expand=True)

# Display the modified DataFrame
print(df)
