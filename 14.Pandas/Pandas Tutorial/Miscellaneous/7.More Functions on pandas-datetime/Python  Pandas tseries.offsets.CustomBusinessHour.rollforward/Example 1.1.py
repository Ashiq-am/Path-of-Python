# Adding the offset to the given timestamp
new_timestamp = ts + cbh

# Print the updated timestamp
print(new_timestamp)

# roll forward if not on offset
result = cbh.rollforward(pd.Timestamp('2019-4-28 11:15:00'))

# print the result
print(result)
