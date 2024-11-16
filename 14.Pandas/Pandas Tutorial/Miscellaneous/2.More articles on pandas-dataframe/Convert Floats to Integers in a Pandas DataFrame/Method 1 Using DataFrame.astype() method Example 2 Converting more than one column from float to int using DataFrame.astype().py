# displaying the datatypes
display(df.dtypes)

# converting 'Weight' and 'Salary' from float to int
df = df.astype({"Weight":'int', "Salary":'int'})

# displaying the datatypes
display(df.dtypes)
