# Display the Output
display(df)
display(df1)

# Selecting old value
a = df['first_set'][4]

# Selecting new value
b = df1['first_set'][1]

# replace values of one DataFrame with
# the value of another DataFrame
df = df.replace(a,b)

# Display the Output
display(df)
