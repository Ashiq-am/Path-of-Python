# Python3 code to demonstrate
# K occurrence element Test
# using sum() + list comprehension

# initializing list
test_list = [1, 3, 5, 5, 4, 5]

# printing original list
print("The original list is : " + str(test_list))

# initializing k
k = 3

# initializing N
N = 5

# using sum() + list comprehension
# K occurrence element Test
res = 0
res = sum([1 for i in test_list if i == N]) == k
if res == 1:
    res = True
else:
    res = False

# printing result
print("Does N occur K times ? : " + str(res))
