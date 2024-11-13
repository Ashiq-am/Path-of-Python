# import the enchant module
import enchant

# Hindi dictionary
tag = "hi_IN"

# check whether Hindi(hi_IN)
# dictionary exists or not
exists = enchant.dict_exists(tag)
if exists == True:
	print("The dictionary for " + tag + " exists.")
else:
	print("The dictionary for " + tag + " does not exists.")
