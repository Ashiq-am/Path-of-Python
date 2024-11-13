# Python3 code to demonstrate
# inserting K after every Nth number
# using join() + enumerate()

# initializing list
test_list = ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r',
							'g', 'e', 'e', 'k', 's']

# printing original list
print ("The original list is : " + str(test_list))

# initializing k
k = 'x'

# initializing N
N = 3

# using join() + enumerate()
# inserting K after every Nth number
res = list(''.join(i + k * (N % 3 == 2)
		for N, i in enumerate(test_list)))

# printing result
print ("The lists after insertion : " + str(res))
