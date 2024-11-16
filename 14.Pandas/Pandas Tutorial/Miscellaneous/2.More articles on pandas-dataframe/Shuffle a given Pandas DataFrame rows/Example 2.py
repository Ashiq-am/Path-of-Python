# import the module
import pandas as pd

# create a DataFrame
ODI_runs = {'name': ['Tendulkar', 'Sangakkara', 'Ponting',
                     'Jayasurya', 'Jayawardene', 'Kohli',
                     'Haq', 'Kallis', 'Ganguly', 'Dravid'],
            'runs': [18426, 14234, 13704, 13430, 12650,
                     11867, 11739, 11579, 11363, 10889]}
df1 = pd.DataFrame(ODI_runs)

# print the original DataFrame
print("Original DataFrame :")
display(df1)

# shuffle the DataFrame rows
df2 = df1.sample(frac=1)

# print the shuffled DataFrame
print("\nAfter Shuffle:")
display(df2)
