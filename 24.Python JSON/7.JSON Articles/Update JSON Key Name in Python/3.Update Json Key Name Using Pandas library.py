import pandas as pd

original_json = {'old_key1': 'value1', 'old_key2': 'value2'}
df = pd.DataFrame([original_json])

df = df.rename(columns={'old_key1': 'new_key1', 'old_key2': 'new_key2'})
updated_json = df.to_json(orient='records')[1:-1]
print(updated_json)
