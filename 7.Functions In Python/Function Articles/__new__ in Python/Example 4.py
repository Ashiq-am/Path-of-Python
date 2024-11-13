# Python program to
# demonstrate __new__ method

# class whose object
# is returned
class GeeksforGeeks(object):
    def __str__(self):
        return "GeeksforGeeks"


# class returning object
# of different class
class Geek(object):
    def __new__(cls):
        return GeeksforGeeks()

    def __init__(self):
        print("Inside init")


print(Geek())
