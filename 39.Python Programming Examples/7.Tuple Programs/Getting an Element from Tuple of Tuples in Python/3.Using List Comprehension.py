# Example tuple of tuples
tuple_of_tuples = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# Accessing an element using comprehension
target_element = [element for inner_tuple in tuple_of_tuples for element in inner_tuple if element == 8][0]
print("Using comprehension:", target_element)
