# Python3 code to demonstrate
# Selective Value selection in list of tuples
# using dict() + get() + list comprehension

# initializing list of tuples
test_list = [('Nikhil', 1), ('Akash', 2), ('Akshat', 3), ('Manjeet', 4)]

# initializing selection list
select_list = ['Nikhil', 'Akshat']

# printing original list
print ("The original list is : " + str(test_list))

# printing selection list
print ("The selection list is : " + str(select_list))

# using dict() + get() + list comprehension
# Selective Value selection in list of tuples
temp = dict(test_list)
res = [temp.get(i, 0) for i in select_list]

# printing result
print ("The selective values of keys : " + str(res))
