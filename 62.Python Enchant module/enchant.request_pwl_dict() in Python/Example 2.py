# import the enchant module
import enchant

# the path of the text file
file_path = "PWL.txt"

# printing the contents of the file
print("File contents:")
with open(file_path, 'r') as f:
	print(f.read())

# instantiating the enchant dictionary
# with request_pwl_dict()
pwl = enchant.request_pwl_dict(file_path)

# the word to be added
new_word = "asd"

# checking whether the word is
# in the dictionary
if pwl.check(new_word):
	print("\nThe word "+ new_word + " exists in the dictionary")
else:
	print("\nThe word "+ new_word + " does not exists in the dictionary")

# addin the word to the dictionary
# using add()
pwl.add("asd")

# printing the contents of the file
# after adding the new word
print("\nFile contents:")
with open(file_path, 'r') as f:
	print(f.read())

# checking for whether the word is
# in the dictionary
if pwl.check(new_word):
	print("The word "+ new_word + " exists in the dictionary")
else:
	print("The word "+ new_word + " does not exists in the dictionary")
