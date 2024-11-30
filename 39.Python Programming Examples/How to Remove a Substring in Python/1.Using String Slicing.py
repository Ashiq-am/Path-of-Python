# Using slicing to remove substring by index
s = "Python is fun"

index = s.find("is ")
if index != -1:
    index = s[:index] + s[index + len("is "):]
    print(index)