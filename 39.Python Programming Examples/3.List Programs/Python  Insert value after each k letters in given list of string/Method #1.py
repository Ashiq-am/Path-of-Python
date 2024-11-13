# Python program to insert value after
# each k letters in given list of string
list1 = ['p', 'y', 't', 'h', 'o', 'n']

# printing original list
print ("Original list : " + str(list1))

# initializing k
k = 'G'

# initializing N
N = 2

# using join() + enumerate()
# inserting K after every Nth number
output = list(''.join(i + k * (N % 2 == 1)
		for N, i in enumerate(list1)))

# printing result
print ("The lists after insertion : " + str(output))
