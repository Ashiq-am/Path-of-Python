my_list = [10, 20, 30, 40, 50]

# Initialize variables for total sum and index
total_sum = 0
index = 0

# Iterate through the list using a while loop
while index < len(my_list):
	total_sum = total_sum + my_list[index]
	index += 1

# Print the final total
print(total_sum)
