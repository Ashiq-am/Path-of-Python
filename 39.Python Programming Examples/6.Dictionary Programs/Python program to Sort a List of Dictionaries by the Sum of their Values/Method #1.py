# Python3 code to demonstrate working of
# Sort Dictionaries by Values Sum
# Using sort() + sum() + values()

def values_sum(row):
    # return values sum
    return sum(list(row.values()))


# initializing list
test_list = [{1: 3, 4: 5, 3: 5}, {1: 7, 10: 1, 3: 10}, {1: 100}, {8: 9, 7: 3}]

# printing original list
print("The original list is : " + str(test_list))

# performing sort
test_list.sort(key=values_sum)

# printing result
print("Sorted Dictionaries List : " + str(test_list))
