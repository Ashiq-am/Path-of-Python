# getting the list of StructFields
field = df.schema.fields

# using for loop to iterate and enumerate
# for indexing or numbering
for count, col_name in enumerate(field, 1):
    # printing the column names
    print(count, "-", col_name.name)

    # visualizing the datframe
    df.show()
