# initializing list
test_list = ["434", "823", "98", "74"]

# printing original list
print("The original list is : " + str(test_list))

# checking all elements to be numeric using isdigit()
# map() to extend to each element
res = all(map(str.isdigit, test_list))

# printing result
print("Are all strings digits ? : " + str(res))
