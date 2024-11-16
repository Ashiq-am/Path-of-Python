# Adding the dateoffset to the given timestamp
new_timestamp = ts + do

# Print the updated timestamp
print(new_timestamp)

# Now we will create a copy of the given
# DateOffset object.
do_copy = do.copy()

# Check if the two objects are same or not
print(do_copy is do)
