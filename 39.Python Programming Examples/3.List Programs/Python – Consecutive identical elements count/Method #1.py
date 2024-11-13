# Python3 code to demonstrate working of
# Consecutive identical elements count
# Using loop + set()

# initializing list
test_list = [4, 5, 5, 5, 5, 6, 6, 7, 8, 2, 2, 10]

# printing original list
print("The original list is : " + str(test_list))

res = []
for idx in range(0, len(test_list) - 1):

    # getting Consecutive elements
    if test_list[idx] == test_list[idx + 1]:
        res.append(test_list[idx])

# getting count of unique elements
res = len(list(set(res)))

# printing result
print("Consecutive identical elements count : " + str(res))
