#importing pandas as pd
import pandas as pd

data = {
	'Date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03']),
	'Sales': [101, 201, 301],
	'Profit': [909, 1809, 2709]
}

df = pd.DataFrame(data)

#Using dt.strftime() method by passing the specific string format as an argument.
df['Date'] = df['Date'].dt.strftime('%d-%m-%Y')
print(df)
df.info()
