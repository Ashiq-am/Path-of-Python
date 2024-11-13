import pandas as pd

test_list = [3,5,4,3,3,4,5,2]

df1 = pd.Series(test_list).value_counts().sort_index().reset_index().reset_index(drop=True)
df1.columns = ['Element', 'Frequency']

# Orignal list
print(f"The original list : {test_list}" )

# printing result
print(f"The list frequency of elements is :\n {df1.to_string(index=False)}" )
