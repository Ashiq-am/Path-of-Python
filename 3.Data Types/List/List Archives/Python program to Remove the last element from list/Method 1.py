# Input List
input_list = [1, 4, 6, 3, 5, 8]

print("The original list is : " + str(input_list))

# Using len() + list slicing
# Remove last element
res = input_list[: len(input_list) - 1]

# Printing result
print("The list after removing last element : " + str(res))
