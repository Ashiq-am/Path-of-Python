# Python3 code to demonstrate working of
# Mark duplicate elements
# Using count() + enumerate() + list comprehension + slicing

# initializing list
test_list = ["gfg", "is", "best", "gfg",
             "best", "for", "all", "gfg"]

# printing original list
print("The original list is : " + str(test_list))

# getting count till current using count() and slicing
res = [val + str(test_list[:idx].count(val) + 1) if test_list.count(val) > 1 else val for idx,
                                                                                          val in enumerate(test_list)]

# printing result
print("Duplicates marked List : " + str(res))
