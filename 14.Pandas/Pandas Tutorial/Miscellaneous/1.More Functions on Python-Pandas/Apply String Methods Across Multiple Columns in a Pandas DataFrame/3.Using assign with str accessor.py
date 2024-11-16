import pandas as pd

df = pd.DataFrame({
    'name': ['geeksforgeeks', 'codingforall', 'codewars'],
    'city': ['noida', 'san francisco', 'los angeles']
})

df = df.assign(name=df['name'].str.capitalize(), city=df['city'].str.capitalize())
print(df)
