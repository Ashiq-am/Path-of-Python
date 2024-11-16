# Adding the Business hour offset to the given timestamp
new_timestamp = ts + bh

# Print the updated timestamp
print(new_timestamp)

# check if the offset is
# anchored or not
result = bh.isAnchored()

# print the result
print(result)
