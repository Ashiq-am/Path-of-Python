# Python3 code to demonstrate
# Multiply K to every Nth element
# using list comprehension + enumerate()

# initializing list
test_list = [1, 4, 5, 6, 7, 8, 9, 12]

# printing the original list
print ("The original list is : " + str(test_list))

# initializing N
N = 3

# initializing K
K = 2

# using list comprehension + enumerate()
# Multiply K to every Nth element
res = [i * K if j % N == 0 else i for j, i in enumerate(test_list)]

# printing result
print ("The list after multiplying K to every Nth element : " + str(res))
