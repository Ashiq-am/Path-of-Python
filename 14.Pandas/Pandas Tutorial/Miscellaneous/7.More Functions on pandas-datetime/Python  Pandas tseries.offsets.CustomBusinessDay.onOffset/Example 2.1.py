# Adding the offset to the given timestamp
new_timestamp = ts + cbd

# Print the updated timestamp
print(new_timestamp)

# check if the given timestamp
# is on offset or not
result = cbd.onOffset(pd.Timestamp('2019-4-19 11:15:00'))

# print the result
print(result)
