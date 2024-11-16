# Adding the offset to the given timestamp
new_timestamp = ts + cbh

# Print the updated timestamp
print(new_timestamp)

# roll backward if not on offset
result = cbh.rollback(pd.Timestamp('2019-4-28 11:15:00'))

# print the result
print(result)
