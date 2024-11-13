# Python3 code to demonstrate working of
# Extract dictionaries with Empty String value in K key
# Using list comprehension

# initializing lists
test_list = [{"Gfg": "4", "is": "good", "best": "1"},
             {"Gfg": "", "is": "better", "best": "8"},
             {"Gfg": "9", "is": "CS", "best": "10"}]

# printing original list
print("The original list : " + str(test_list))

# initializing K key
K = "Gfg"

# using list comprehension to fetch empty string key's dictionaries
res = [sub for sub in test_list if sub[K] == '']

# printing result
print("The extracted dictionaries : " + str(res))
