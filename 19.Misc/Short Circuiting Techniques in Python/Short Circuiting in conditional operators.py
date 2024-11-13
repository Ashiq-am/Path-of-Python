# python code to demonstrate short circuiting
# using conditional operators

# helper function
def check(i):
	print ("geeks")
	return i

# using conditional expressions
# since 10 is not greater than 11
# further execution is not taken place
# to check for truth value.
print( 10 > 11 > check(3) )

print ("\r")

# using conditional expressions
# since 11 is greater than 10
# further execution is taken place
# to check for truth value.
# return true as 11 > 3
print( 10 < 11 > check(3) )


print ("\r")


# using conditional expressions
# since 11 is greater than 10
# further execution is taken place
# to check for truth value.
# return false as 11 < 12
print( 10 < 11 > check(12) )
