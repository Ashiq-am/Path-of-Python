# Python program to demonstrate the use of
# count() method using optional parameters

# string in which occurrence will be checked
string = "geeks for geeks"

# counts the number of times substring occurs in
# the given string between index 0 and 5 and returns
# an integer
print(string.count("geeks", 0, 5))

print(string.count("geeks", 0, 15))
