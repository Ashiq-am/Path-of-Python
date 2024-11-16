# importing pandas
import pandas as pd

df = pd.DataFrame({'Last': ['Gaitonde', 'Singh', 'Mathur'],
				'First': ['Ganesh', 'Sartaj', 'Anjali']})

print('Before Join')
print(df, '\n')

print('After join')
df['Name']= df["First"].astype(str) +" "+ df["Last"]
print(df)
