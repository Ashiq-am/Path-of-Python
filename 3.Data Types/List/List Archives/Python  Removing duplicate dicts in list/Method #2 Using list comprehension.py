# Python3 code to demonstrate
# remove duplicate dictionary
# using list comprehension

# initializing list
test_list = [{"Akash" : 1}, {"Kil" : 2}, {"Akshat" : 3}, {"Kil" : 2}, {"Akshat" : 3}]

# printing original list
print ("Original list : " + str(test_list))

# using list comprehension to
# remove duplicates
res_list = [i for n, i in enumerate(test_list) if i not in test_list[n + 1:]]

# printing resultant list
print ("Resultant list is : " + str(res_list))
