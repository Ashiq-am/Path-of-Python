# Python3 code to demonstrate
# to add multiple similar values
# using extend() + list comprehension

# using extend() + list comprehension to add multiple values
# adds 3, 50 times.
res = []
res.extend([3 for i in range(50)])

# printing result
print ("The filtered list is : " + str(res))
