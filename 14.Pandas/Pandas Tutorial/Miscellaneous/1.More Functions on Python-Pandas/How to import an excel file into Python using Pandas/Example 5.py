import pandas as pd
df = pd.read_excel('sample.xlsx',
				na_values =['item1',
							'item2'])
print(df)
