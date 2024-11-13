import re

"""We create a re.MatchObject and store it in 
match_object variable 
the '()' parenthesis are used to define a 
specific group"""

match_object = re.match(r'(\d+)\-(\w+)\-(\w+)',
						'498-ImperialCollege-London')

""" d in above pattern stands for numerical character 
	w in above pattern stands for alphabetical character 
	+ is used to match a consecutive set of characters 
	satisfying a given condition so w+ will match a 
	consecutive set of alphabetical characters 
	d+ will match a consecutive set of numerical characters 
	"""

# generating the tuple with all matched groups
detail_tuple = match_object.groups()

# printing the tuple
print(detail_tuple)
