# import the enchant module
import enchant

# instantiating the dictionary
# without passing any parameter
d = enchant.request_dict()

# finding the dictionary tag
tag = d.tag
print("The dictionary tag is " + tag)
