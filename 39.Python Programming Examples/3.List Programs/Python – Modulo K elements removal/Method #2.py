# Python3 code to demonstrate
# Modulo K elements removal
# using list comprehension

# initializing list
test_list = [1, 9, 4, 7, 6, 5, 8, 3]

# printing original list
print ("The original list is : " + str(test_list))

# initializing K
K = 3

# using list comprehension
# Modulo K elements removal
res = [i for i in test_list if(i % K != 0)]

# printing result
print ("List after removal of modulo K values : " + str(res))
