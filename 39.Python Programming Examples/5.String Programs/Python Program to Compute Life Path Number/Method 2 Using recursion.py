# Python3 code to demonstrate working of
# Life Path Number
# Using recursion

# initializing string
test_str = "19970314"

# printing original string
print("The original string is : " + str(test_str))

# recursion function definition
def lpn(num): return num if num < 10 else lpn(num // 10 + num % 10)

# recursive function initial call
res = lpn(int(test_str))

# printing result
print("Life Path Number : " + str(res))
