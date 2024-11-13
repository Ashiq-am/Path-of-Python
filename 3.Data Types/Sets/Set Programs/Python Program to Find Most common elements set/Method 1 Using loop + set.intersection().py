# Python3 code to demonstrate working of
# Most common elements set
# Using loop + intersection()

# initializing list
test_list = [{4, 3, 5, 2}, {8, 4, 7, 2},
             {1, 2, 3, 4}, {9, 5, 3, 7}]

# printing original list
print("The original list is : " + str(test_list))

# initializing arg_set
arg_set = {9, 6, 5, 3}

res = set()
max_len = 0

for sub in test_list:

    # updating max value on occurrence
    if len(sub.intersection(arg_set)) > max_len:
        max_len = len(sub.intersection(arg_set))
        res = sub

    # printing result
print("Max Set intersection : " + str(res))
