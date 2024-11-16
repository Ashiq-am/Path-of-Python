# Adding the Business hour offset to the given timestamp
new_timestamp = ts + bh

# Print the updated timestamp
print(new_timestamp)

# create a copy
bh_copy = bh.copy()

# Check if both objects are same
print(bh is bh_copy)
