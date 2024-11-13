# Python3 code to demonstrate
# Filling alphabets
# using map()

# initializing empty list
test_list = []

# printing initial list
print ("Initial list : " + str(test_list))

# using map()
# for filling alphabets
test_list = list(map(chr, range(97, 123)))

# printing resultant list
print ("List after insertion : " + str(test_list))
