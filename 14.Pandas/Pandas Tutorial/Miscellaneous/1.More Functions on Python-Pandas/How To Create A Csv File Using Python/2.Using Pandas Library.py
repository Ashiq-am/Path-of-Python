# Step 1 Importing pandas
import pandas as pd

# Step 2 Prepare your data
data = {
	'Name': ['Rajat', 'Tarun', 'Bobby'],
	'Age': [30, 25, 35],
	'City': ['New York', 'Delhi', 'Pune']
}

# Step 3 Create a DataFrame using DataFrame function
df = pd.DataFrame(data)

# Step 4 Specify the file path to save data
csv_file_path = 'data.csv'

# Step 5 Write the DataFrame to a CSV file using to_csv() function where file path is passed
df.to_csv(csv_file_path, index=False)

print(f'CSV file "{csv_file_path}" has been created successfully.')
