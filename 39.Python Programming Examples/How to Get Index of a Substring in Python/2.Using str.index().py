# Using index() method
s1 = "Welcome to Python programming"
s2 = "Python"

# using try..except to handle exception,
# in case substring is not found
try:
    sub = s1.index(s2)
    print(sub)

except ValueError:
    print("Substring not found")