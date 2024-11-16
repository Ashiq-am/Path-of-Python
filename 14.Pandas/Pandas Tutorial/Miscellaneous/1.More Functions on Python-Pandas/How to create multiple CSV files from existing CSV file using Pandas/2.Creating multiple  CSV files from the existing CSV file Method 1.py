import pandas as pd

# read DataFrame
data = pd.read_csv("Customers.csv")

# no of csv files with row size
k = 2
size = 5

for i in range(k):
	df = data[size*i:size*(i+1)]
	df.to_csv(f'Customers_{i+1}.csv', index=False)

df_1 = pd.read_csv("Customers_1.csv")
print(df_1)

df_2 = pd.read_csv("Customers_2.csv")
print(df_2)
