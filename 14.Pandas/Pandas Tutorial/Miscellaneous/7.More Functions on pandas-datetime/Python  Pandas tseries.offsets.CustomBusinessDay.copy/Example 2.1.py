# Adding the offset to the given timestamp
new_timestamp = ts + cbd

# Print the updated timestamp
print(new_timestamp)

# now create a copy of the given offset object.
cbd_copy = cbd.copy()

# check if the copies are same
print(cbd_copy is cbd)
