import pandas as pd

df = pd.DataFrame({
    'name': ['GeeksForGeeks', 'CodingForAll', 'CodeWars'],
    'score': [85, 90, 78],
    'city': ['Noida', 'San Francisco', 'Los Angeles']
})

first_row = df[df['score'] > 80].head(1).iloc[0]
print(first_row)
