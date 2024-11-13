# import the enchant module
import enchant

# dictionary of en_US
d = enchant.request_dict("en_US")

# the dictionary tag
tag = d.tag
print("The dictionary tag is " + tag)
