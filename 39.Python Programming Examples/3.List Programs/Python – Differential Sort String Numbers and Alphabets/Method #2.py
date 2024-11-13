# Python3 code to demonstrate working of
# Differential Sort String Numbers and Alphabets
# Using sorted() + isnumeric()

# initializing list
test_list = ["100", "G", "74", "L", "98", "M", "4"]

# printing original list
print("The original list is : " + str(test_list))

# using int() to type convert to integer
# using sorted() to perform sort operation
res = sorted(test_list, key = lambda ele: (ele.isnumeric(), int(ele) if ele.isnumeric() else ele))

# printing result
print("The Custom sorted result : " + str(res))
