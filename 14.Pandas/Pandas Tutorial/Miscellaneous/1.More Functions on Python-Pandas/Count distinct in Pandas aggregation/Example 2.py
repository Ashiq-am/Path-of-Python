# import module
import pandas as pd
import numpy as np

# create Data frame
df = pd.DataFrame({'Order Date': ['2021-02-22',
								'2021-02-22',
								'2021-02-22',
								'2021-02-24',
								'2021-02-24'],
				'Product Id': ['021', '021',
								'022', '022', '022'],
				'Order Quantity': [23, 22, 22,
									45, 10]})

# print original Dataframe
print(df)

# let's Count distinct in Pandas aggregation
df = df.groupby("Order Date").agg({"Order Quantity": np.sum,
								"Product Id": pd.Series.nunique})

# print final output
print(df)
