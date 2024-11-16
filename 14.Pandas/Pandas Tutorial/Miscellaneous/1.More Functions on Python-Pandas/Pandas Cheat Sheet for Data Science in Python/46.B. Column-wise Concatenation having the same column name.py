data = {'DISCOUNT': [5, 7, 10, 8, 6]}

# Create Pandas Dataframe with dictionary
discount = pd.DataFrame(data)

# Concatenate df2 and discount
df = pd.concat([df2, discount], axis=1)
print(df)
