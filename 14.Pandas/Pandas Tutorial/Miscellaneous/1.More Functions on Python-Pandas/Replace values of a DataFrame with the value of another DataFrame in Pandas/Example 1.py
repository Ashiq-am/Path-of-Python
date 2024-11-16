# selecting old value
a = df1['first_set'][4]

# selecting new value
b = df['first_set'][1]


# replace values of one DataFrame
# with the value of another DataFrame
df1 = df1.replace(a,b)

# Display the Output
display(df1)
