# Python program to understand about locals

# here no local variable is present
def demo1():
    print("Here no local variable is present : ", locals())


# here local variables are present
def demo2():
    name = "Ankit"
    print("Here local variables are present : ", locals())
    print("Before updating name is : ", name)

    # trying to change name value
    locals()['name'] = "Sri Ram"

    print("after updating name is : ", name)


# driver code
demo1()
demo2()
