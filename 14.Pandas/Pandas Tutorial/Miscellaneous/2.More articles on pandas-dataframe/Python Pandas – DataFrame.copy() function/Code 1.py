import pandas as pd

#Create Series
s = pd.Series([3,4,5],['earth','mars','jupiter'])
k = pd.Series([1,2,3],['earth','mars','jupiter'])

#Create DataFrame df from two series
df = pd.DataFrame({'mass':s,'diameter':k})

df
