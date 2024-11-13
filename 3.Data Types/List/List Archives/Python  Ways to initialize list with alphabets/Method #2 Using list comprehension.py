# Python3 code to demonstrate
# Filling alphabets
# using list comprehension

# initializing empty list
test_list = []

# printing initial list
print ("Initial list : " + str(test_list))

# using list comprehension
# for filling alphabets
test_list = [chr(x) for x in range(ord('a'), ord('z') + 1)]

# printing resultant list
print ("List after insertion : " + str(test_list))
