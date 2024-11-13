# Python3 code to demonstrate working of
# Convert delimiter seperated Mixed String to valid List
# Using eval() + split() + list comprehension

# initializing string
test_str = "6# 2# 9#[3, 5, 6]#(7, 8)# 8# 4# 10"

# printing original string
print("The original string is : " + str(test_str))

# initializing delim
delim = "#"

# encapsulating entire result in list comprehension
res = [eval(ele) for ele in test_str.split(delim)]

# printing result
print("List after conversion : " + str(res))
