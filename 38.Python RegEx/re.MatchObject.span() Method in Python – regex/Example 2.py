# import library
import re

""" 
We create a re.MatchObject and 
store it in match_object variable, 
'()' parenthesis are used to define a 
specific group"""

match_object = re.match(r'(\d+)',
                        'geeks')

""" 
d in above pattern stands for numerical character 
+ is used to match a consecutive set of characters 
satisfying a given condition so d+ will match a 
consecutive set of numerical characters 
"""

# generating the tuple with the
# starting and ending index
print(match_object.span())
