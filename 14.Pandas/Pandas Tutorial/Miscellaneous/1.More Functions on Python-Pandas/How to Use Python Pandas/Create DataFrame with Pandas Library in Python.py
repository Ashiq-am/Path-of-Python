import pandas as pd

# Define data as a dictionary
data = {
    'Name': ['Sangita', 'Rohan', 'Max'],
    'Age': [25, 30, 35],
    'Gender': ['Female', 'Male', 'Male']
}

# Create DataFrame
df = pd.DataFrame(data)

print(df)
