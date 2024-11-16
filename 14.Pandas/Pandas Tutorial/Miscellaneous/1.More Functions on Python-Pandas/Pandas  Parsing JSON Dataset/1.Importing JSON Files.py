import pandas as pd
# Creating Dataframe
df = pd.DataFrame([['a', 'b'], ['c', 'd']],
				index =['row 1', 'row 2'],
				columns =['col 1', 'col 2'])

# Indication of expected JSON string format
print(df.to_json(orient ='split'))

print(df.to_json(orient ='index'))
