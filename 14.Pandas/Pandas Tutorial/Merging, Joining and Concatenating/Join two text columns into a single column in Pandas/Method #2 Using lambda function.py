# importing pandas
import pandas as pd

df = pd.DataFrame({'Last': ['Gaitonde', 'Singh', 'Mathur'],
				'First': ['Ganesh', 'Sartaj', 'Anjali']})

print('Before Join')
print(df, '\n')

print('After join')
df['Name'] = df[['First', 'Last']].apply(lambda x: ' '.join(x), axis = 1)
print(df)
