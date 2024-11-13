# Python3 code to demonstrate working of
# Embedded Numbers Summation in String List
# Using join() + loop

# initializing list
test_list = ['g4fg', 'i4s5', 'b9e4st']

# printing original list
print("The original list is : " + str(test_list))

# Embedded Numbers Summation in String List
# Using join() + loop
res = 0
for sub in test_list:
    res += int(''.join(chr for chr in sub if chr.isdigit()))

# printing result
print("The summation of strings : " + str(res))
