import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Rahul', 'Riya', 'Rohit'],
    'Age': [25, 30, 35],
    'Gender': ['Male', 'Female', 'Male']
}

df = pd.DataFrame(data)

# Remove the 'Gender' column
df.drop(columns=['Gender'], inplace=True)

print(df)
