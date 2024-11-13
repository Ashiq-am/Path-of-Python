# Python3 code to demonstrate
# check for minimum N occureneces of K
# using sum() + list comprehension

# initializing list
test_list = [1, 3, 5, 5, 4, 5]

# printing original list
print("The original list is : " + str(test_list))

# initializing k
k = 5

# initializing N
N = 3

# using sum() + list comprehension
# checking occurrences of K atleast N times
res = 0
res = sum([1 for i in test_list if i == k]) >= N
if res == 1:
    res = True
else:
    res = False

# printing result
print("Does %d occur atleast %d times ? :" % (k, N) + str(res))
