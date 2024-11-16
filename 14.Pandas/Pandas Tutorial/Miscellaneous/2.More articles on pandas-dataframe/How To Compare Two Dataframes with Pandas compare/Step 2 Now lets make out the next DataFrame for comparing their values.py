# creating the second dataFrame by
# copying and modifying the first DataFrame
second_df = first_df.copy()

# loc specifies the location,
# here 0th index of Price Column
second_df.loc[0, 'Price'] = 150
second_df.loc[1, 'Price'] = 70
second_df.loc[2, 'Price'] = 30
second_df.loc[0, 'Quantity'] = 15
second_df.loc[1, 'Quantity'] = 7
second_df.loc[2, 'Quantity'] = 6

# display the df
second_df
