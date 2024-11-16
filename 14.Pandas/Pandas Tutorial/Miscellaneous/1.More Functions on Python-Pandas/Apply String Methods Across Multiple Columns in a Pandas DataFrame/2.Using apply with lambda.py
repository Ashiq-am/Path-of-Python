import pandas as pd

df = pd.DataFrame({
    'name': ['GeeksForGeeks', 'CodingForAll', 'CodeWars'],
    'city': ['Noida', 'San Francisco', 'Los Angeles']
})

df['name'] = df['name'].apply(lambda x: x.upper())
df['city'] = df['city'].apply(lambda x: x.upper())
print(df)
