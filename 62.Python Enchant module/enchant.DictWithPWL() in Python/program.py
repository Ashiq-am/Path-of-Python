# import the enchant module
import enchant

# dictionary with only en_US
d = enchant.Dict("en_US")

# the word to be searched
word = "gfg"

# check whether the word is in the dictionary
if d.check(word):
	print("The word "+ word + " exists in the dictionary")
else:
	print("The word "+ word + " does not exists in the dictionary")

# the path of the text file
file_path = "PWL.txt"

# instantiating the enchant dictionary
# with DictWithPWL()
d = enchant.DictWithPWL("en_US", file_path)

# checking whether the word is
# in the new dictionary
if d.check(word):
	print("\nThe word "+ word + " exists in the dictionary")
else:
	print("\nThe word "+ word + " does not exists in the dictionary")
