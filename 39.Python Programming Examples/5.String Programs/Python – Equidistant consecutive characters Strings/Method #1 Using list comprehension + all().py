# Python3 code to demonstrate working of
# Equidistant consecutive characters Strings
# Using list comprehension + all()

# initializing list
test_list = ["abcd", "egil", "mpsv", "abd"]

# printing original list
print("The original list is : " + str(test_list))

# ord() used to get ASCII value
res = [sub for sub in test_list if all(ord(
	sub[idx + 1]) - ord(sub[idx]) == ord(sub[1]) - ord(sub[0]) for idx in range(0, len(sub) - 1))]

# printing result
print("Filtered Strings : " + str(res))
