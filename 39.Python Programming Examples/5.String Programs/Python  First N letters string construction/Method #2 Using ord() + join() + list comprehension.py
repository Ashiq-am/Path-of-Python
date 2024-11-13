# Python3 code to demonstrate
# First N letters string construction
# using join() + list comprehension + ord()

# initializing N
N = 15

# using join() + list comprehension + ord()
# First N letters string construction
res = ''.join(chr(ord('a') + i) for i in range(N))

# print result
print("The string after construction : " + str(res))
