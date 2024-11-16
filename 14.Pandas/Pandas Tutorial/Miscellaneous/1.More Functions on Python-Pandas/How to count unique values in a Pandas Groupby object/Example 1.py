# import pandas
import pandas as pd

# create dataframe
df = pd.DataFrame({'Col_1': ['a', 'b', 'c', 'b', 'a', 'd'],
				'Col_2': [1, 2, 3, 3, 2, 1]})

# print original dataframe
print("original dataframe:")
display(df)


# call groupby method.
df = df.groupby("Col_1")

# call agg method
df = df.agg({"Col_2": "nunique"})

# call reset_index method
df = df.reset_index()

# print dataframe
print("final dataframe:")
display(df)
