# import the enchant module
import enchant

# the path of the text file
file_path = "PWL.txt"

# instantiating the enchant dictionary
# with request_pwl_dict()
pwl = enchant.request_pwl_dict(file_path)

# checking whether the words are
# in the new dictionary
print(pwl.check("gfg"))
