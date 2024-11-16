# joining new column in dataframe
# endwith function used to check
df['GFG_Emp'] = list(
    map(lambda x: x.endswith('gfg.com'), df['Company_Emp_id']))

# printing new data frame
df
