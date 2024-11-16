# joining new column in dataframe
# .startswith function used to check
df['GFG_Emp'] = list(
    map(lambda x: x.endswith('Infosys'), df['Company']))

# printing new data frame
df
