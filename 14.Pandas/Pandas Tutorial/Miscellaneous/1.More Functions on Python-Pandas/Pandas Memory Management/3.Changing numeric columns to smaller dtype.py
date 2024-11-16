import pandas as pd
df = pd.read_csv('data.csv')

# Downcasting float64 to float16
df['price'].memory_usage()

df['price'] = df['price'].astype('float16')
df['price'].memory_usage()
