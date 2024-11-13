# Python3 code to demonstrate
# Custom length Matrix
# using zip() + list comprehension

# initializing list
test_list = ['a', 'b', 'c']

# initializing counter list
counter_list = [1, 4, 2]

# printing original list
print ("The original list is : " + str(test_list))

# printing counter list
print ("The counter list is : " + str(counter_list))

# using zip() + list comprehension
# Custom length Matrix
res = [[i] * j for i, j in zip(test_list, counter_list)]

# printing result
print ("The custom length matrix is : " + str(res))
