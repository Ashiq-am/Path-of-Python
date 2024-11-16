def custom_merge(row):
    return pd.Series({
        'key': row['key'],
        'value1': row['value_x'],
        'value2': row['value_y']
    })

merged_temp = pd.merge(df1, df2, on='key', how='inner')
merged_df = merged_temp.apply(custom_merge, axis=1)
print(merged_df)
