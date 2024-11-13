# Python3 code to demonstrate working of
# Equidistant element list
# using list comprehension

# initializing start value
strt = 5

# initializing end value
end = 10

# initializing length
length = 8

# Equidistant element list
# using list comprehension
test_list = [strt + x * (end - strt)/length for x in range(length)]

# Printing result
print("The Equidistant list is : " + str(test_list))
