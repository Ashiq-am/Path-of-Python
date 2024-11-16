# Adding the Business hour offset to the given timestamp
new_timestamp = ts + bh

# Print the updated timestamp
print(new_timestamp)

# Move the timestamp to next
# business day
result = ts + bh.next_bday

# Print the result
print(result)
