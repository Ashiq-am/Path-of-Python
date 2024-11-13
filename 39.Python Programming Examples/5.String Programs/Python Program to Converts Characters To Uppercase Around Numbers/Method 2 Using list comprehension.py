# initializing string
test_str = 'geeks4geeks is best1 for ge8eks'

# printing original string
print("The original string is : " + str(test_str))

# list comprehension offering 1 liner solution
res = ''.join(
    [test_str[idx].upper() if test_str[idx + 1].isdigit() or test_str[idx - 1].isdigit() else test_str[idx] for idx in
     range(len(test_str) - 1)])

# printing result
print("Transformed String : " + str(res))
