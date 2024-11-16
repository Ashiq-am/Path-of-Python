# import pandas
import pandas as pd
# Sample DataFrame
data = {
  'ID': [1, 2, 3],
  'Details': [{'Name': 'Monu', 'Age': 30},
              {'Name': 'Sonu', 'Age': 25},
              {'Name': 'Golu', 'Age': 35}]
}

df = pd.DataFrame(data)

# Accessing and extracting values from 'Details' column
df['Name'] = df['Details'].apply(lambda x: x['Name'])
df['Age'] = df['Details'].apply(lambda x: x['Age'])

print(df)
