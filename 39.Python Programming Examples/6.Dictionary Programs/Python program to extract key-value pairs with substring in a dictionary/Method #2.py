# Python3 code to demonstrate working of
# Dictionaries with Substring values
# Using map() + in operator

# initializing lists
test_list = [{"Gfg": "4", "best": "1"},
			{"Gfg": "good for CS", "best": "8"},
			{"Gfg": "good CS content", "best": "10"}]

# printing original list
print("The original list : " + str(test_list))

# initializing K key
K = "Gfg"

# initializing target value
val = "CS"

# map() used to perform filtering
res = list(map(lambda sub: val in sub[K], test_list))
res = [test_list[idx] for idx, ele in enumerate(res) if res[idx]]

# printing result
print("Dictionaries with particular substring values : " + str(res))
