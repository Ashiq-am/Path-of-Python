# Adding the Business hour offset to the given timestamp
new_timestamp = ts + bh

# Print the updated timestamp
print(new_timestamp)

# check if the passed date is
# on offset or not
result = bh.onOffset(pd.to_datetime('2010-02-12 11:00:00'))

# print the result
print(result)
