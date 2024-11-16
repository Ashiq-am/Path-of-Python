import pandas as pd
import numpy as np

# Create a DataFrame
df1 = {
	'Name':['abc','bcd','cde','def','efg','fgh','ghi'],
'Math_score':[52,87,49,74,28,59,48]}

df1 = pd.DataFrame(df1, columns=['Name','Math_score'])

# Computing Cumulative Percentage
df1['cum_percent'] = 100*(df1.Math_score.cumsum() / df1.Math_score.sum())

df1
