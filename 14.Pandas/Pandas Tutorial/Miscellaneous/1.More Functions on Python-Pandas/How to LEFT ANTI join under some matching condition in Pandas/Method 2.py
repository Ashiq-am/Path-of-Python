# code
import pandas as pd

# inverse of semi-join:
# creating dataframes using pd.DataFrame() method.
df1 = pd.DataFrame({
	"city": ["new york", "chicago", "orlando", 'mumbai'],
	"temperature": [21, 14, 35, 30],
	"humidity": [65, 68, 75, 75],
})
df2 = pd.DataFrame({
	"city": ["chicago", "new york", "orlando"],
	"humidity": [67, 60, 70]
})

# carrying out anti join using merge method
df3 = df1.merge(df2, on='city')

df = df1[~df1['city'].isin(df3['city'])]

print(df)
