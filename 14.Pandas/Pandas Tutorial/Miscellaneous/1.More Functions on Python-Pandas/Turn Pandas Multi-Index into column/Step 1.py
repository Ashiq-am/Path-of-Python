import pandas as pd

# Creating index for muti-index dataframe
tuples = [('A', 'a'), ('A', 'b'), ('B', 'a'), ('B', 'b')]
index = pd.MultiIndex.from_tuples(tuples)

# Value corresponding to the index
data = [2, 4, 6, 8]

# Creating dataframe using 'data' and 'index'
df = pd.DataFrame(data = data, index = index, columns = ['value'])
print(df)
