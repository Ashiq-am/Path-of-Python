# Here string2 is the default string used
def fun2(string1, string2="Geeks"):
	print(string1 + string2)


# Thiscan be a way where no order is needed.
fun2(string2='GeeksFor', string1="Geeks")

# since we are not mentioning the non-default argument
# so it will give error.
fun2(string2='GeeksFor')
