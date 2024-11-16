# Let's create an empty list to store the values
# of average mpg for each cylinder
avg_mpg = []

# c is the current cylinder size
for c in unique_cyl:
	# for storing the sum of mpg
	mpgbycyl = 0
	# for storing the sum of cylinder
	# in each category
	cylcount = 0

	# iterate over all the data in mpg
	for x in mpg_data:
		# Check if current value matches c
		if x['cylinders']== c:
			# Add the mpg values for c
			mpgbycyl += float(x['mpg'])
			# increment the count of cylinder
			cylcount += 1

	# Find the average mpg for size c
	avg = mpgbycyl/cylcount
	# Append the average mpg to list
	avg_mpg.append((c, avg))

# Sort the list
avg_mpg.sort(key = lambda x : x[0])

# Print the list
print(avg_mpg)
