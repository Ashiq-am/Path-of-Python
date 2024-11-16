# creating the mask variable with appropriate
# condition
mask_var = df['Degree'] =='MBA'

# creating a dataframe
df1_mask = df[mask_var]

print(df1_mask)
