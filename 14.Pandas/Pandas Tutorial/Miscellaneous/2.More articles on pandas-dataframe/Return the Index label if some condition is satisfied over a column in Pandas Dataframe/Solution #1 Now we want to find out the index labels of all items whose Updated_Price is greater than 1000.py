# Select all the rows which satisfies the criteria
# convert the collection of index labels to list.
Index_label = df[df['Updated Price']>1000].index.tolist()

# Print all the labels
print(Index_label)
