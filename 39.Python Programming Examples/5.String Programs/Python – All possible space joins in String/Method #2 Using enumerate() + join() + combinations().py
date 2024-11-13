# Python3 code to demonstrate working of
# All possible space joins in String
# Using enumerate() + join() + combinations()
import itertools

# initializing string
test_str = 'Geeksforgeeks is best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# All possible space joins in String
# Using enumerate() + join() + combinations()
res = []
temp = test_str.split(' ')
N = range(len(temp) - 1)
for idx in N:
    for sub in itertools.combinations(N, idx + 1):
        temp1 = [val + " " if i in sub else val for i, val in enumerate(temp)]
        temp2 = "".join(temp1)
        res.append(temp2)

    # printing result
print("All possible spaces List : " + str(res))
