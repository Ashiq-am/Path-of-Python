# Using the df.apply() function on product column
df['Product'] = df['Product'].apply(lambda x : x.strip().capitalize())

# Print the Dataframe
print(df)





"""
to format the Product names in the right format. 
Inside the Pandas DataFrame.apply() function we will use lambda function.

"""
