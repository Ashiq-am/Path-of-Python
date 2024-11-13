# Python3 code to demonstrate working of
# Print Alphabets till N
# Using loop

# initialize N
N = 20

# printing N
print("Number of elements required : " + str(N))

# Print Alphabets till N
# Using loop
res = ""
for idx in range(97, 97 + N):
    res = res + chr(idx)

# printing result
print("Alphabets till N are : " + str(res))
