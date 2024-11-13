import pandas as pd

data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 22}]
df = pd.DataFrame(data)
filtered_data = df.loc[df['age'] > 25].to_dict('records')
print(filtered_data)
