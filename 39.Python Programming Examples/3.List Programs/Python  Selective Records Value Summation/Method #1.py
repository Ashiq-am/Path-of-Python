# Python3 code to demonstrate
# Selective Records Value Summation
# using dict() + get() + list comprehension + sum()

# initializing list of tuples
test_list = [('Nikhil', 1), ('Akash', 2), ('Akshat', 3), ('Manjeet', 4)]

# initializing selection list
select_list = ['Nikhil', 'Akshat']

# printing original list
print ("The original list is : " + str(test_list))

# printing selection list
print ("The selection list is : " + str(select_list))

# using dict() + get() + list comprehension + sum()
# Selective Records Value Summation
temp = dict(test_list)
res = sum([temp.get(i, 0) for i in select_list])

# printing result
print ("The selective values summation of keys : " + str(res))
