import pandas as pd

df1 = pd.DataFrame({'id': ['A01', 'A02', 'A03', 'A04'],
					'Name': ['ABC', 'PQR', 'DEF', 'GHI']})

df3 = pd.DataFrame({'City': ['MUMBAI', 'PUNE', 'MUMBAI', 'DELHI'],
					'Age': ['12', '13', '14', '12']})

# the default behaviour is join='outer'
# inner join

result = pd.concat([df1, df3], axis=1, join='inner')
display(result)
