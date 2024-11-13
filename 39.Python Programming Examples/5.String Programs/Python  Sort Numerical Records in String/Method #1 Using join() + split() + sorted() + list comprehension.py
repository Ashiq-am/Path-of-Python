# Python3 code to demonstrate working of
# Sort Numerical Records in String
# Using join() + split() + sorted() + list comprehension

# initializing string
test_str = "Akshat 15 Nikhil 20 Akash 10"

# printing original string
print("The original string is : " + test_str)

# Sort Numerical Records in String
# Using join() + split() + sorted() + list comprehension
temp1 = test_str.split()
temp2 = [temp1[idx : idx + 2] for idx in range(0, len(temp1), 2)]
temp3 = sorted(temp2, key = lambda ele: (int(ele[1]), ele[0]))
res = ' '.join([' '.join(ele) for ele in temp3])

# printing result
print("The string after sorting records : " + res)
