import pandas as pd

# Sample dictionary
data = {'A': [(1, 'x'), (2, 'y'), (3, 'z')],
		'B': [(4, 'p'), (5, 'q'), (6, 'r')]}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

print(df)
