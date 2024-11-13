# Python3 code to demonstrate working of
# Convert delimiter seperated Mixed String to valid List
# Using loop + split() + eval()

# initializing string
test_str = "6# 2# 9#[3, 5, 6]#(7, 8)# 8# 4# 10"

# printing original string
print("The original string is : " + str(test_str))

# initializing delim
delim = "#"

# spliting using split()
temp = test_str.split(delim)
res = []

# using loop + eval() to convert to
# required result
for ele in temp:
    res.append(eval(ele))

# printing result
print("List after conversion : " + str(res))
