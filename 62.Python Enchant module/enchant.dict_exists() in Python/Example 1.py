# import the enchant module
import enchant

# American English dictionary
tag = "en_US"

# check whether American English(en_US)
# dictionary exists or not
exists = enchant.dict_exists(tag)
if exists == True:
	print("The dictionary for " + tag + " exists.")
else:
	print("The dictionary for " + tag + " does not exists.")
