import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Rahul', 'Raksha', 'Mohit'],
    'Age': [25, 30, 35],
    'Gender': ['Male', 'Female', 'Male']
}

df = pd.DataFrame(data)

# Define data for the new row
new_row = {'Name': 'Sakshi', 'Age': 28, 'Gender': 'Female'}

# Append the new row to the DataFrame
df = df.append(new_row, ignore_index=True)

print(df)
