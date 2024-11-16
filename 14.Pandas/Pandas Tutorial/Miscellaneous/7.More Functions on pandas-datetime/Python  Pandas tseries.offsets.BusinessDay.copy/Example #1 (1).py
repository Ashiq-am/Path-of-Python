# Adding the Business day offset to the given timestamp
new_timestamp = ts + bd

# Print the updated timestamp
print(new_timestamp)

# create a copy of the given
# offset object
bd_copy = bd.copy()

# Check if the two objects are
# same or not
print(bd_copy is bd)
