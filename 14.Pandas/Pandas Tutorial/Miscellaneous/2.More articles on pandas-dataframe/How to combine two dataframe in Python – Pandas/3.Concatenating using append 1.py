import pandas as pd
# First DataFrame
df1 = pd.DataFrame({'id': ['A01', 'A02', 'A03', 'A04'],
					'Name': ['ABC', 'PQR', 'DEF', 'GHI']})

# Second DataFrame
df2 = pd.DataFrame({'id': ['B05', 'B06', 'B07', 'B08'],
					'Name': ['XYZ', 'TUV', 'MNO', 'JKL']})

df3 = pd.DataFrame({'City': ['MUMBAI', 'PUNE', 'MUMBAI', 'DELHI'],
					'Age': ['12', '13', '14', '12']})


# appending multiple DataFrame
result = df1.append([df2, df3])
display(result)
