import pandas as pd

nested_dict = {'A': {'score': 85, 'age': 25},
               'B': {'score': 92, 'age': 30},
               'C': {'score': 78, 'age': 22}}

df = pd.DataFrame.from_dict(nested_dict, orient='index')

sorted_df = df.sort_values(by=['score', 'age'])

sorted_nested_dict = sorted_df.to_dict(orient='index')

print(sorted_nested_dict)
