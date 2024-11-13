# Example using list comprehension
original_list = [1, 2, 3, 4, 5]
new_lists = [[item * i for i in range(1, 4)] for item in original_list]

# Output
print(new_lists)
