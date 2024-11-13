# Python3 code to demonstrate working of
# Extract Suffix numbers
# Using loop + isdigit() + slicing

# initializing string
test_str = "GFG04"

# printing original string
print("The original string is : " + str(test_str))

# loop for fetching the 1st non digit index
rev_str = test_str[::-1]
temp_idx = 0

for idx, ele in enumerate(rev_str):
    if not ele.isdigit():
        temp_idx = idx
        break

# reversing the extracted string to
# get number
res = rev_str[:temp_idx][::-1]

# printing result
print("Suffix number : " + str(res))
