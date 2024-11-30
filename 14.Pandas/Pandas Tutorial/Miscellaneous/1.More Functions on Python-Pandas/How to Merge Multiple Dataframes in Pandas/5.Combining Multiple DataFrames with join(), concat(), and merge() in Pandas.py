import pandas as pd

df1 = pd.DataFrame({'Species': ['Rose', 'Tulip', 'Lily'],'Color': ['Red', 'Yellow', 'White']})
df2 = pd.DataFrame({'Species': ['Rose', 'Tulip', 'Orchid'],'Price': [2.5, 3.0, 5.0]})
df3 = pd.DataFrame({'Species': ['Rose', 'Tulip', 'Jasmine'],'Scent': ['Fragrant', 'Mild', 'Intense']})
df4 = pd.DataFrame({'Species': ['Rose', 'Lily', 'Orchid', 'Jasmine'],'Region': ['Europe', 'Asia', 'Tropics', 'Asia']})

# 1. Using merge(): Merge all DataFrames on 'Species' column
merged_df = pd.merge(df1, df2, on='Species', how='inner')
merged_df = pd.merge(merged_df, df3, on='Species', how='inner')
merged_df = pd.merge(merged_df, df4, on='Species', how='inner')
print("Merge Example:")
print(merged_df)

# 2. Using join(): Join all DataFrames on 'Species' column (first set as index)
df1.set_index('Species', inplace=True)
df2.set_index('Species', inplace=True)
df3.set_index('Species', inplace=True)
df4.set_index('Species', inplace=True)
joined_df = df1.join(df2, how='inner').join(df3, how='inner').join(df4, how='inner')
print("\nJoin Example:")
print(joined_df)

# 3. Using concat(): Concatenate all DataFrames horizontally (along columns)
concat_df = pd.concat([df1.reset_index(), df2.reset_index(), df3.reset_index(), df4.reset_index()], axis=1)
print("\nConcat Example:")
print(concat_df)