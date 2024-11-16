# Create an empty list
Row_list = []

# Iterate over each row
for rows in df.itertuples():
    # Create list for the current row
    my_list = [rows.Date, rows.Event, rows.Cost]

    # append the list to the final list
    Row_list.append(my_list)

# Print the list
print(Row_list)
