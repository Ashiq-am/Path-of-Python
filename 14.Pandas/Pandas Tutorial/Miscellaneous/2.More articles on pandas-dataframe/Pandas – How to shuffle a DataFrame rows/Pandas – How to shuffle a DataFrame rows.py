# import the modules
import pandas as pd
import numpy as np

# create a DataFrame
ODI_runs = {'name': ['Tendulkar', 'Sangakkara', 'Ponting',
					'Jayasurya', 'Jayawardene', 'Kohli',
					'Haq', 'Kallis', 'Ganguly', 'Dravid'],
			'runs': [18426, 14234, 13704, 13430, 12650,
					11867, 11739, 11579, 11363, 10889]}
df = pd.DataFrame(ODI_runs)

# print the original DataFrame
print("Original DataFrame :")
print(df)

# shuffle the DataFrame rows
df = df.sample(frac = 1)

# print the shuffled DataFrame
print("\nShuffled DataFrame:")
print(df)
