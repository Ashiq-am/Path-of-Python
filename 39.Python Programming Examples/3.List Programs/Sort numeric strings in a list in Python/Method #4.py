# Python3 code to demonstrate
# numeric string sorting
# using sorted () + key with (len (x), x)

# initializing list
test_list = [ '4', '6', '7', '2', '1']

# printing original list
print ("The original list is : " + str (test_list))

# using sorted () + key with (len (x), x)
# numeric string sorting
res = sorted (test_list, key = lambda x: (len (x), x))

# printing result
print ("The resultant sorted list : " + str (res))
