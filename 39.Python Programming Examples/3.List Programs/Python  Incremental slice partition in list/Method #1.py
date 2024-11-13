# Python3 code to demonstrate working of
# Incremental slice partition in list
# Using loop

# initializing list
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# printing original list
print("The original list is : " + str(test_list))

# Incremental slice partition in list
# Using loop
res = {}
N = 1
strt = 0
while strt < len(test_list):
	res[N] = test_list[strt : strt + N]
	strt += N
	N += 1

# printing result
print("The partitioned dictionary from list is : " + str(res))
