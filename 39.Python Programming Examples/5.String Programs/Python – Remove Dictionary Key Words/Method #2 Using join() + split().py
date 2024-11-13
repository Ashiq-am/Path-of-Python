# Python3 code to demonstrate working of
# Remove Dictionary Key Words
# Using join() + split()

# initializing string
test_str = 'gfg is best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing Dictionary
test_dict = {'geeks' : 1, 'best': 6}

# Remove Dictionary Key Words
# Using join() + split()
temp = test_str.split(' ')
temp1 = [word for word in temp if word.lower() not in test_dict]
res = ' '.join(temp1)

# printing result
print("The string after replace : " + str(res))
