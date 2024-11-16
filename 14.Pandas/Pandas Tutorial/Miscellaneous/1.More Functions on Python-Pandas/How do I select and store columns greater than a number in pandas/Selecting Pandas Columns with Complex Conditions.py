# Custom function to filter columns
def custom_condition(col):
    return (col > 20).any() and (col < 60).all()

# Applying the custom function
df_custom_filtered = df.loc[:, df.apply(custom_condition)]
print(df_custom_filtered)
