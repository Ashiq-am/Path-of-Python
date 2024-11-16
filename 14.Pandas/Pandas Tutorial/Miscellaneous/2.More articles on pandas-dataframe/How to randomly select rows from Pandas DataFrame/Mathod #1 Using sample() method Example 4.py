# fraction of rows

# here you get 70 % row from the df
# make put into another dataframe df1
df1 = df.sample(frac =.7)

# Now select 50 % rows from df1
df1.sample(frac =.50)
