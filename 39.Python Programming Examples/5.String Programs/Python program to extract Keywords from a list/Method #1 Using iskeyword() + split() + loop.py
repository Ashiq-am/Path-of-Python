# Python3 code to demonstrate working of
# Extract Keywords from String List

# Using iskeyword() + loop + split()
import keyword

# initializing list
test_list = ["Gfg is True", "Gfg will yield a return",
			"Its a global win", "try Gfg"]

# printing original list
print("The original list is : " + str(test_list))


# iterating using loop
res = []
for sub in test_list:
    for word in sub.split():

        # check for keyword using iskeyword()
        if keyword.iskeyword(word):
            res.append(word)

# printing result
print("Extracted Keywords : " + str(res))
