# Python program to demonstrate
# passing dictionary as kwargs


def display(x=0, y=0, **name):
    print(name["fname"] + " " + name["mname"] + " " + name["lname"])
    print("x =", x)
    print("y =", y)


def main():
    # passing dictionary key-value
    # pair with other arguments
    display(2, fname="John", mname="F.", lname="Kennedy")


# Driver's code
main()
