# Python 3 code to demonstrate
# Alternate String to Integer Conversion
# using naive method

# initializing list
test_list = ['1', '4', '3', '6', '7']

# Printing original list
print("Original list is : " + str(test_list))

# using naive method to
# perform conversion
for i in range(0, len(test_list)):
    if i % 2:
        test_list[i] = int(test_list[i])

# Printing modified list
print("Modified list is : " + str(test_list))
