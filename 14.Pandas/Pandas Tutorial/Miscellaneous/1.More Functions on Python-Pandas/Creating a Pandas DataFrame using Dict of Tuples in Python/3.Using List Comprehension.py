import pandas as pd

# Original dictionary with tuples
data_dict = {'Key1': ('A', 10), 'Key2': ('B', 20), 'Key3': ('C', 30)}

# Creating a DataFrame using list comprehension
df = pd.DataFrame([(key,) + values for key, values in data_dict.items()],
				columns=['Index', 'Column1', 'Column2']).set_index('Index')

# Displaying the DataFrame
print(df)
