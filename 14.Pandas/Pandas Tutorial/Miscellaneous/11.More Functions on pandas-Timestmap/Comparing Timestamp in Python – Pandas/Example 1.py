# Compare first and second timestamps
if df['new_time'][0] <= df['new_time'][1]:
	print("First entry is old")
else:
	print("Second entry is old")
