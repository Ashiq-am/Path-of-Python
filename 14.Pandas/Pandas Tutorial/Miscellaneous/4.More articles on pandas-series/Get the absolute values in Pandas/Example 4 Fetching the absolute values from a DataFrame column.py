# import the library
import pandas as pd

# create the DataFrame
df = pd.DataFrame({'p' : [2, 3, 4, 5],
				'q' : [10, 20, 30, 40],
				'r' : [200, 60, -40, -60]})
display(df)

# fetching the absolute values
print("\nThe absolute values are :")
display(df.r.abs())
