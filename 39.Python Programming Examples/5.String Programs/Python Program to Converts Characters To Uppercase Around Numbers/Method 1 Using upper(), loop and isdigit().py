# initializing string
test_str = 'geeks4geeks is best1 for ge8eks'

# printing original string
print("The original string is : " + str(test_str))

res = ''
for idx in range(len(test_str) - 1):
    if test_str[idx + 1].isdigit() or test_str[idx - 1].isdigit():
        res += test_str[idx].upper()
    else:
        res += test_str[idx]

    # printing result
print("Transformed String : " + str(res))
