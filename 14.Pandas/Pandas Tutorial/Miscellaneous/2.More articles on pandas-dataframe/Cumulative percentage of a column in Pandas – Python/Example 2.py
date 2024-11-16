import pandas as pd
import numpy as np

# Create a DataFrame
df1 = {
	'Name':['abc','bcd','cde','def','efg','fgh','ghi'],
'Math_score':[52,87,49,74,28,59,48],
'Eng_score':[34,67,25,89,92,45,86]
}

df1 = pd.DataFrame(df1,columns=['Name','Math_score','Eng_score'])

# Computing cumulative Percentage
df1['Eng_cum_percent'] = (df1.Eng_score.cumsum() / df1.Eng_score.sum()) * 100

df1
