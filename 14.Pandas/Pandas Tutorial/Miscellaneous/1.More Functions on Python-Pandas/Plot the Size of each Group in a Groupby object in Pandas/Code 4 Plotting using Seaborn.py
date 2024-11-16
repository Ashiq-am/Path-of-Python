# use the groupby() function to group island column
# and apply size() function
# size() is equivalent to couting the distinct rows
result = dataset.groupby(['island']).size()

# plot the result
sns.barplot(x = result.index, y = result.values)
