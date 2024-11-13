# create a set of allowed characters
allowed_chars = set(("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"))

# input string
string = "inv@lid"

# convert string into set of characters
validation = set((string))

# check condition
if validation.issubset(allowed_chars):
    print("True")

else:
    print("False")
