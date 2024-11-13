# Python3 code to demonstrate working of
# Convert Float to digit list
# using list comprehension + isdigit()

# initialize N
N = 6.456

# printing N
print("The floating number is : " + str(N))

# Convert Float to digit list
# using list comprehension + isdigit()
res = [int(ele) for ele in str(N) if ele.isdigit()]

# printing result
print("List of floating numbers is : " + str(res))
