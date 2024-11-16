# import pandas
import pandas as pd
# Sample DataFrame
data = {
  'ID': [1, 2, 3],
  'Details': [{'Name': 'Monu', 'Age': 30},
              {'Name': 'sonu', 'Age': 25},
              {'Name': 'Golu', 'Age': 35}]
}

df = pd.DataFrame(data)

# Accessing and extracting values from 'Details' column
df['Name'] = [i['Name'] for i in df['Details']]
df['Age'] = [i['Age'] for i in df['Details']]

print(df)
