import timeit

# Inefficient loop
start_time = timeit.default_timer()
my_list = []
for i in range(1, 1000000):
    my_list.append(i * 2)
end_time = timeit.default_timer()
print("Time taken (inefficient loop):", end_time - start_time)

# Efficient list comprehension
start_time = timeit.default_timer()
my_list = [i * 2 for i in range(1, 1000000)]
end_time = timeit.default_timer()
print("Time taken (efficient list comprehension):", end_time - start_time)
