# Python3 code to demonstrate
# First N letters string construction
# using join() + list comprehension

# initializing N
N = 15

# using join() + list comprehension
# First N letters string construction
res = ''.join(['% c' % x for x in range(97, 97 + N)])

# print result
print("The string after construction : " + str(res))
