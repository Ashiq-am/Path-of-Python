# Python3 code to demonstrate
# remove duplicate dictionary
# using frozenset

# initializing list
test_list = [{"Akash" : 1}, {"Kil" : 2}, {"Akshat" : 3}, {"Kil" : 2}, {"Akshat" : 3}]

# printing original list
print ("Original list : " + str(test_list))

# using frozenset to
# remove duplicates
res_list = {frozenset(item.items()) : item for item in test_list}.values()

# printing resultant list
print ("Resultant list is : " + str(res_list))
