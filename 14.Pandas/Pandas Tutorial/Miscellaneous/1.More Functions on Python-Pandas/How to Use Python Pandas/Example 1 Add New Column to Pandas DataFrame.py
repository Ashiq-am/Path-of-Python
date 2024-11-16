import pandas as pd
# Create a DataFrame
data = {
    'Name': ['Rahul', 'Mahi', 'Ram'],
    'Age': [25, 30, 35],
    'Gender': ['Male', 'Female', 'Male']
}

df = pd.DataFrame(data)

# Add a new column 'Location'
df['Location'] = ['Delhi', 'Banglore', 'Noida']

print(df)
