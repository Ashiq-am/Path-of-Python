# Python3 code to demonstrate working of
# Mark duplicate elements
# Using map() + count() + lambda

# initializing list
test_list = ["gfg", "is", "best", "gfg",
             "best", "for", "all", "gfg"]

# printing original list
print("The original list is : " + str(test_list))

# getting count till current using count() and slicing
res = list(
    map(lambda ele: ele[1] + str(test_list[: ele[0]].count(ele[1]) + 1) if test_list.count(ele[1]) > 1 else ele[1],
        enumerate(test_list)))

# printing result
print("Duplicates marked List : " + str(res))
