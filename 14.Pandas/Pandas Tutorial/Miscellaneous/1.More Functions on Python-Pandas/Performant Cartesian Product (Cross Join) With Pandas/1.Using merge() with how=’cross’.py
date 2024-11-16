import pandas as pd

# Step 1: Create DataFrames
df1 = pd.DataFrame({'A': [1, 2], 'B': ['X', 'Y']})
df2 = pd.DataFrame({'C': ['a', 'b'], 'D': [3, 4]})

# Step 2: Perform Cartesian Product
result = pd.merge(df1, df2, how='cross')

# Step 3: Explore the Result
print("DF1: \n",df1)
print("DF2: \n",df2)
print("Cross join: \n",result)
