# Python3 code to demonstrate
# Bigram formation
# using zip() + split() + list comprehension

# initializing list
test_list = ['geeksforgeeks is best', 'I love it']

# printing the original list
print ("The original list is : " + str(test_list))

# using zip() + split() + list comprehension
# for Bigram formation
res = [i for j in test_list
	for i in zip(j.split(" ")[:-1], j.split(" ")[1:])]

# printing result
print ("The formed bigrams are : " + str(res))
