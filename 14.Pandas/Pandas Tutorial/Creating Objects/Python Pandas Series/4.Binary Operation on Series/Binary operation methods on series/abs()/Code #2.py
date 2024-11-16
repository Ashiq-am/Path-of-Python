# importing pandas module
import pandas as pd

df = pd.DataFrame({'Name': ['John', 'Hari', 'Peter', 'Loani'],
				'Age': [31, 29, 57, 40],
				'val': [98, 48, -80, -14]})


df['ope'] = (df.val - 87).abs()

df
