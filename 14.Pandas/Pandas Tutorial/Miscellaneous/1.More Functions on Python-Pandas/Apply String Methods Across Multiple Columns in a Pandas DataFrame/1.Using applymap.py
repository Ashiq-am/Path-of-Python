import pandas as pd

df = pd.DataFrame({
    'name': ['GeeksForGeeks', 'CodingForAll', 'CodeWars'],
    'city': ['Noida', 'San Francisco', 'Los Angeles']
})

df[['name', 'city']] = df[['name', 'city']].applymap(lambda x: x.lower())
print(df)
