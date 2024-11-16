# Adding the offset to the given timestamp
new_timestamp = ts + cbd

# Print the updated timestamp
print(new_timestamp)

# roll forward if the given timestamp
# is not on offset
result = cbd.rollforward(pd.Timestamp('2019-4-21 11:15:00'))

# print the result
print(result)
