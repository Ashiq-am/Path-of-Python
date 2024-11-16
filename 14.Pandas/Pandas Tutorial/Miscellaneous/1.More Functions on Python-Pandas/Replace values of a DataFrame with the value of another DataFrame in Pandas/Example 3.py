#selected value
a = df['first_set'][4]
b = df1['second_set'][1]

# replace values of one DataFrame with
# the value of another DataFrame
df = df.replace(a,'Hello')

# replace values of one DataFrame with
# the value of another DataFrame
df1 = df1.replace(b,'Geeks')


display (df)
display(df1)
