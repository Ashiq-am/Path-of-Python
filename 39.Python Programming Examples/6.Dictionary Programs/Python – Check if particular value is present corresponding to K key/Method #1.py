# Python3 code to demonstrate working of
# Check if particular value is present corrresponding to K key
# Using list comprehension

# initializing lists
test_list = [{"Gfg": "4", "is": "good", "best": "1"},
             {"Gfg": "find", "is": "better", "best": "8"},
             {"Gfg": "9", "is": "CS", "best": "10"}]

# printing original list
print("The original list : " + str(test_list))

# initializing K key
K = "Gfg"

# initializing target value
val = "find"

# extracting values using list comprehension
# using in operator to check for values
res = val in [sub[K] for sub in test_list]

# printing result
print("Is key-val pair present? : " + str(res))
