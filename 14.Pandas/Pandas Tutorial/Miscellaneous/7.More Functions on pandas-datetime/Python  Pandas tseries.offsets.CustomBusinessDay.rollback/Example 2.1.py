# Adding the offset to the given timestamp
new_timestamp = ts + cbd

# Print the updated timestamp
print(new_timestamp)

# roll back if the given timestamp
# is not on offset
result = cbd.rollback(pd.Timestamp('2019-4-21 11:15:00'))

# print the result
print(result)
