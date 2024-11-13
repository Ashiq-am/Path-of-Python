import re

"""We create a re.MatchObject and store it in 
match_object variable 
the '()' parenthesis are used to define a 
specific group"""

match_object = re.match(r'(\w+)@(\w+)\.(\w+)', 'username@geekforgeeks.org')

""" w in above pattern stands for alphabetical character 
	+ is used to match a consecutive set of characters 
	satisfying a given condition 
	so w+ will match a consecutive set of alphabetical characters"""

# Following line will raise IndexError exception
print(match_object.group(7))
