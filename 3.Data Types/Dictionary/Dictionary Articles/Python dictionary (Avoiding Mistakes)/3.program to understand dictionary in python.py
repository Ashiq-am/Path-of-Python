# program to understand dictionary in python

# creating an empty dictionary
mydictionary ={}

# inserting values in dictionary
mydictionary ={'greeting':'Hello',
			'status':'how are you',
			'thanks':'thanks visit again'}

# print values according to choice
print(mydictionary['greeting'])
print(mydictionary['status'])
print(mydictionary['thanks'])

# this will print none
print(mydictionary.get('college'))

# this will throw an error
print(mydictionary['college'])
