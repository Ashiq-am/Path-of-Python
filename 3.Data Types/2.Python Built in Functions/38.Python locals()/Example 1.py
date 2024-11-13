# Python program to understand about locals
# here no local variable is present

def demo1():
	print("Here no local variable is present : ", locals())

# here local variables are present
def demo2():
	name = "Ankit"
	print("Here local variables are present : ", locals())

# driver code
demo1()
demo2()
