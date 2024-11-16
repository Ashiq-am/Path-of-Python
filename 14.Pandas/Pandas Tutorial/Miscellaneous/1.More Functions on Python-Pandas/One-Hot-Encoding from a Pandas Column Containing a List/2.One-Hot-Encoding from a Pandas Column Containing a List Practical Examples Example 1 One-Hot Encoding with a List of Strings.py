import pandas as pd

data = {
    'ID': [1, 2, 3],
    'Colors': [['Red', 'Blue'], ['Green'], ['Red', 'Green', 'Blue']]
}
df = pd.DataFrame(data)

one_hot = pd.get_dummies(df['Colors'].apply(pd.Series).stack()).groupby(level=0).sum()
df_one_hot = df.drop('Colors', axis=1).join(one_hot)

print(df_one_hot)
