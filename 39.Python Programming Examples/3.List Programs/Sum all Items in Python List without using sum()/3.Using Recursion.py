my_list = [10, 20, 30, 40, 50]

# Define a recursive function to calculate the sum
def find_sum(lst):
	if len(lst) == 0:
		return 0
	else:
		return lst[0] + find_sum(lst[1:])

# Calculate the sum using the recursive function
total_sum = find_sum(my_list)

# Print the total sum
print(total_sum)
