# Adding the Business hour offset to the given timestamp
new_timestamp = ts + bh

# Print the updated timestamp
print(new_timestamp)

# roll forward the date if not
# on offset
result = bh.rollforward( pd.to_datetime('2010-02-12 11:00:00'))

# print the result
print(result)
