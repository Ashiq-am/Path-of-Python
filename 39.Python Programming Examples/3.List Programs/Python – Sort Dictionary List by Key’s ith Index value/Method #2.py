# Python3 code to demonstrate working of
# Sort Dictionary List by Key's ith Index value
# Using sort() + lambda + get()

# initializing lists
test_list = [{"Gfg" : "Best", "for" : "Geeks"},
			{"Gfg" : "Good", "for" : "Me"},
			{"Gfg" : "Better", "for" : "All"}]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = "Gfg"

# initializing i
i = 2

# using sort to perform sort(), lambda
# function drives conditions, get() used to
# avoid missing key error
res = sorted(test_list, key = lambda sub: sub.get(K)[i])

# printing result
print("List after sorting : " + str(res))
