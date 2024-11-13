# Python3 code to demonstrate working of
# Interconvert Horizontal and Vertical String
# using [Vertical to Horizontal] using replace() + "\n"

# initializing string
test_str = 'g\ne\ne\nk\ns\nf\no\nr\ng\ne\ne\nk\ns\n'

# printing original String
print("The original string is : " + str(test_str))

# using replace() + "\n" to solve this problem
res = test_str.replace("\n", "")

# printing result
print("The converted string : " + str(res))
