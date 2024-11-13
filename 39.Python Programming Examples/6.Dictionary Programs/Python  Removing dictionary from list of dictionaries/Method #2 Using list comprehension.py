# Python3 code to demonstrate
# to delete dictionary in list
# using list comprehension

# initializing list of dictionaries
test_list = [{"id" : 1, "data" : "HappY"},
			{"id" : 2, "data" : "BirthDaY"},
			{"id" : 3, "data" : "Rash"}]

# printing original list
print ("The original list is : " + str(test_list))

# using list comprehension
# to delete dictionary in list
res = [i for i in test_list if not (i['id'] == 2)]

# printing result
print ("List after deletion of dictionary : " + str(res))
