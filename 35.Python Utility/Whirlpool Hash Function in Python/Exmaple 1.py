# Python program to demonstrate
# whirlpool hash function


import whirlpool

string = b"GeeksforGeeks"

h1 = whirlpool.new(string)
hashed_output = h1.hexdigest()

print("The hashed value is")
print(hashed_output)
