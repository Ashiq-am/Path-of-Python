# Python3 code to demonstrate
# Min / Max in heterogenous list
# using list comprehension + min()/max() + isinstance()

# initializing list
test_list = [3, 'computer', 5, 'geeks', 6, 7]

# printing original list
print ("The original list is : " + str(test_list))

# using list comprehension + min()/max() + isinstance()
# Min / Max in heterogenous list
res = min(i for i in test_list if isinstance(i, int))

# printing result
print ("The minimum value in list is : " + str(res))
