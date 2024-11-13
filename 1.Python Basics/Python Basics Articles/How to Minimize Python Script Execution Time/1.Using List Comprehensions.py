import timeit

# approach using set
start_time = timeit.default_timer()
my_set = set(range(1, 1000000))
element_to_find = 999999
result = element_to_find in my_set
end_time = timeit.default_timer()
print("Time taken (inefficient):", end_time - start_time)

# Efficient approach
start_time = timeit.default_timer()
my_list = list(range(1, 1000000))
element_to_find = 999999
result = element_to_find in my_list
end_time = timeit.default_timer()
print("Time taken (efficient):", end_time - start_time)
