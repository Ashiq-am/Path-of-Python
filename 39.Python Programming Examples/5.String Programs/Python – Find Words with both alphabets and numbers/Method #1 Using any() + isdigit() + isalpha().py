# Python3 code to demonstrate working of
# Words with both alphabets and numbers
# Using isdigit() + isalpha() + any()

# initializing string
test_str = 'geeksfor23geeks is best45 for gee34ks and cs'

# printing original string
print("The original string is : " + test_str)

# Words with both alphabets and numbers
# Using isdigit() + isalpha() + any()
res = []
temp = test_str.split()
for idx in temp:
    if any(chr.isalpha() for chr in idx) and any(chr.isdigit() for chr in idx):
        res.append(idx)

    # printing result
print("Words with alphabets and numbers : " + str(res))
