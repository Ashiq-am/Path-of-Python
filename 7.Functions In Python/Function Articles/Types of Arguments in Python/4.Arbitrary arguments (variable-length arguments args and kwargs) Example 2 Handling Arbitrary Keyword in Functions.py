# Python program to illustrate
# **kwargs for variable number of keyword arguments

def fun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Driver code
fun(course="DSA", platform="GeeksforGeeks", difficulty="easy")