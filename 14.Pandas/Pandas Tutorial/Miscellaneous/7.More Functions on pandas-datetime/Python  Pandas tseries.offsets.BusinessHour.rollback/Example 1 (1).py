# Adding the Business hour offset to the given timestamp
new_timestamp = ts + bh

# Print the updated timestamp
print(new_timestamp)

# rollback the date if not
# on offset
result = bh.rollback( pd.to_datetime('2010-02-13'))

# print the result
print(result)
