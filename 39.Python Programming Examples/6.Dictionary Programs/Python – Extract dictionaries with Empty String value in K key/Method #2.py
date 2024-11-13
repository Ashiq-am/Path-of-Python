# Python3 code to demonstrate working of
# Extract dictionaries with Empty String value in K key
# Using filter() + lambda

# initializing lists
test_list = [{"Gfg": "4", "is": "good", "best": "1"},
             {"Gfg": "", "is": "better", "best": "8"},
             {"Gfg": "9", "is": "CS", "best": "10"}]

# printing original list
print("The original list : " + str(test_list))

# initializing K key
K = "Gfg"

# filter() used to iteration
# lambda for functionality
res = list(filter(lambda sub: sub[K] == '', test_list))

# printing result
print("The extracted dictionaries : " + str(res))
