# displaying the datatypes
display(df.dtypes)

# converting 'Field_2' and 'Field_3' from float to int
df['Field_2'] = df['Field_2'].apply(np.int64)
df['Field_3'] = df['Field_3'].apply(np.int64)

# displaying the datatypes
display(df.dtypes)
