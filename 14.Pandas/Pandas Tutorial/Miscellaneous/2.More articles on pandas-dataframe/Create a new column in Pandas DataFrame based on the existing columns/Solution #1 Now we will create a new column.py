# using apply function to create a new column
df['Discounted_Price'] = df.apply(lambda row: row.Cost -
								(row.Cost * 0.1), axis = 1)

# Print the DataFrame after addition
# of new column
print(df)




"""

called ‘Discounted_Price’ after applying a 10% discount on the 
existing ‘Cost’ column

"""
