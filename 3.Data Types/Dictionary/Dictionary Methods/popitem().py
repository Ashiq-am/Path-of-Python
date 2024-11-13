''''''



'''Code #1 : Demonstrating the use of popitem()'''



# Python 3 code to demonstrate
# working of popitem()

# initializing dictionary
test_dict = { "Nikhil" : 7, "Akshat" : 1, "Akash" : 2 }

# Printing initial dict
print ("The dictionary before deletion : " + str(test_dict))

# using popitem() to return + remove arbitrary
# pair
res = test_dict.popitem()

# Printing the pair returned
print ('The arbitrary pair returned is : ' + str(res))

# Printing dict after deletion
print ("The dictionary after removal : " + str(test_dict))









"""Practical Application: This particular function can be used to formulate the random name for playing a game 
or deciding the random ranklist without using any random function."""








'''Code #2 : Demonstrating application of popitem()'''




# Python 3 code to demonstrate
# application of popitem()

# initializing dictionary
test_dict = { "Nikhil" : 7, "Akshat" : 1, "Akash" : 2 }

# Printing initial dict
print ("The dictionary before deletion : " + str(test_dict))

n = len(test_dict)

# using popitem to assign ranks
for i in range(0, n) :
	print ("Rank " + str(i + 1) + " " + str(test_dict.popitem()))

# Printing end dict
print ("The dictionary after deletion : " + str(test_dict))
