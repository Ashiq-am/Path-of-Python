import pandas as pd

data = {'A': ['apple', 'potato', 'orange']}
df = pd.DataFrame(data)
print("Before Replacing\n", df)

def replace_values(x):
	if x == 'apple' or x == 'orange':
		return 'fruit'
	elif x == 'potato':
		return 'vegetable'
	else:
		return x
df['A'] = df['A'].apply(replace_values)
print("After Replacing\n", df)
