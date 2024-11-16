# importing pandas as pd
import pandas as pd

# creating the dataframe using pandas DataFrame
df = pd.DataFrame({'X':[1, 2, 3, 4, 5],
				'Y':[54, 12, 57, 48, 96],
				'Z':['a', 'b', 'c', 'd', 'e']})

# eval('expression') calculates the sum of the specified columns of that row
df = df.eval('Sum = X + Y')
print(df)
