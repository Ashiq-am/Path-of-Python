original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Example condition: remove even numbers
condition = lambda x: x % 2 == 0

filtered_list = [x for x in original_list if not condition(x)]
print(filtered_list)
