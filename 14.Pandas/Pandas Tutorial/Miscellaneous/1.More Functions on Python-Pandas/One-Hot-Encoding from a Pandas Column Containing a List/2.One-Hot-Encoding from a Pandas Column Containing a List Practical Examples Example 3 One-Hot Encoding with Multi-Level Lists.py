data = {
    'ID': [1, 2, 3],
    'Categories': [['Fruit:Apple', 'Fruit:Banana'], ['Fruit:Orange', 'Vegetable:Carrot'], ['Meat:Chicken']]
}
df = pd.DataFrame(data)

df['Categories'] = df['Categories'].apply(lambda x: [item.split(':')[-1] for item in x])  # Get subcategories
one_hot = pd.get_dummies(df['Categories'].apply(pd.Series).stack()).groupby(level=0).sum()

df_one_hot = df.drop('Categories', axis=1).join(one_hot)

print(df_one_hot)
