# Generate random array
arr_len = 50
arr = [random.randint(1, win_height) for i in range(arr_len)]

# Initialize sorted and unsorted parts of array
sorted_idx = -1
unsorted_idx = 0
