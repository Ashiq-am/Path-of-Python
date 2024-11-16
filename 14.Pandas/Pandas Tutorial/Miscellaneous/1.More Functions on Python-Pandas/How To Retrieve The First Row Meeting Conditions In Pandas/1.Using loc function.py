import pandas as pd

df = pd.DataFrame({
    'name': ['GeeksForGeeks', 'CodingForAll', 'CodeWars'],
    'score': [85, 90, 78],
    'city': ['Noida', 'San Francisco', 'Los Angeles']
})

first_row = df.loc[df['score'] > 80].iloc[0]
print(first_row)
