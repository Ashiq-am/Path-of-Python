# Python3 code to demonstrate
# Selective Value selection in list of tuples
# using next() + list comprehension

# initializing list of tuples
test_list = [('Nikhil', 1), ('Akash', 2), ('Akshat', 3), ('Manjeet', 4)]

# initializing selection list
select_list = ['Nikhil', 'Akshat']

# printing original list
print ("The original list is : " + str(test_list))

# printing selection list
print ("The selection list is : " + str(select_list))

# using next() + list comprehension
# Selective Value selection in list of tuples
res = [next((sub[1] for sub in test_list
	if sub[0] == i), 0) for i in select_list]

# printing result
print ("The selective values of keys : " + str(res))
