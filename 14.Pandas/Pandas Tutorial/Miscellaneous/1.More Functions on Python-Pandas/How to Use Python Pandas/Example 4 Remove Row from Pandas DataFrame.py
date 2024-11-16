import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Mohit', 'Sonal', 'Rishav'],
    'Age': [25, 30, 35],
    'Gender': ['Male', 'Female', 'Male']
}

df = pd.DataFrame(data)

# Remove the row where Name is 'Mohit'
df = df[df['Name'] != 'Mohit']

print(df)
