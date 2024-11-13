# Python3 code to demonstrate
# getting selective dictionary keys
# using list comprehension

# initializing dictionary
test_dict = {"Akash" : 1, "Akshat" : 2, "Nikhil" : 3, "Manjeet" : 4}

# initializing selective list keys
select_list = ['Manjeet', 'Nikhil']

# printing original dictionary
print ("The original dictionary is : " + str(test_dict))

# printing selective list
print ("The selective list is : " + str(select_list))

# using list comprehension
# getting selective dictionary keys
res = [test_dict[i] for i in select_list if i in test_dict]

# printing result
print ("The selected values from list keys is : " + str(res))
