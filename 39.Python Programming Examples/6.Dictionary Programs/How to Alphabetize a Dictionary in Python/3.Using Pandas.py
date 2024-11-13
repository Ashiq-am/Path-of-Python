import pandas as pd

# Original dictionary
my_dict = {'banana': 3, 'apple': 4, 'cherry': 2, 'date': 5}

# Convert dictionary to pandas DataFrame
df = pd.DataFrame(list(my_dict.items()), columns=['Key', 'Value'])

# Sort DataFrame by keys
df_sorted_by_keys = df.sort_values(by='Key')

# Convert DataFrame back to dictionary
sorted_dict = dict(df_sorted_by_keys.values)

print(sorted_dict)
