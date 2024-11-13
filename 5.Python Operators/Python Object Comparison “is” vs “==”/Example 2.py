# Python program to demonstrate working of
# "is"

# Two different objects having same values
x1 = [10, 20, 30]
x2 = [10, 20, 30]

# We get "No" here
if x1 is x2:
	print("Yes")
else:
	print("No")

# It creates another reference x3 to same list.
x3 = x1

# So we get "Yes" here
if x1 is x3:
	print("Yes")
else:
	print("No")

# "==" would also produce yes anyway
if x1 == x3:
	print("Yes")
else:
	print("No")
