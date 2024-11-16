import pandas as pd

# Step 1: Read the CSV file into a DataFrame
csv_file_path = 'mon.csv'
df = pd.read_csv(csv_file_path)

# Step 2: Define the values for the new "City" column
new_city_values = ['New York', 'Los Angeles', 'Chicago', 'San Francisco']

# Step 3: Add the new "City" column to the DataFrame
df['City'] = new_city_values

# Step 4: Write the DataFrame back to the CSV file
df.to_csv(csv_file_path, index=False)
