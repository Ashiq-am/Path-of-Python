# Adding the offset to the given timestamp
new_timestamp = ts + cbh

# Print the updated timestamp
print(new_timestamp)

# check if the given timestamp is
# on offset or not
result = cbh.onOffset(pd.Timestamp('2019-4-28 11:15:00'))

# print the result
print(result)
