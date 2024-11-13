# Python3 code to demonstrate the
# working of set() on dictionary

# initializing list
dic1 = { 4 : 'geeks', 1 : 'for', 3 : 'geeks' }

# Printing dictionary before conversion
# internally sorted
print("Dictionary before conversion is : " + str(dic1))

# Dictionary after conversion are
# notice lost keys
print("Dictionary after conversion is : " + str(set(dic1)))
