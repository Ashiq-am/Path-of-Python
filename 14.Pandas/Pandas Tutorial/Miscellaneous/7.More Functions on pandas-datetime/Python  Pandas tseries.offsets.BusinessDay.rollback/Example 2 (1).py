# Adding the Business day offset to the given timestamp
new_timestamp = ts + bd

# Print the updated timestamp
print(new_timestamp)

# roll the provided date backward if not
# on the offset
date = bd.rollback(dt = pd.to_datetime('2010-02-13'))

# print the date
print(date)
