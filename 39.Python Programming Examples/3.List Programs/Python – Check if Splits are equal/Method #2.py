# Python3 code to demonstrate working of
# Check if Splits are equal
# Using split() + all()

# initializing string
test_str = '45# 45# 45# 45# 45'

# printing original string
print("The original string is : " + str(test_str))

# initializing splt_chr
splt_chr = "#"

# splitting using split()
new_list = test_str.split(splt_chr)

# checking all equal to 1st element
res = all(ele == new_list[0] for ele in new_list)

# printing result
print("Are all splits equal ? : " + str(res))
