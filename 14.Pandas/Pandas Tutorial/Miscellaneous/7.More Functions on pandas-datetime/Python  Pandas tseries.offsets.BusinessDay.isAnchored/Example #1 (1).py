# Adding the Business day offset to the given timestamp
new_timestamp = ts + bd

# Print the updated timestamp
print(new_timestamp)

# check if the offset is
# anchored or not
result = bd.isAnchored()

# print the result
print(result)
