# import the enchant module
import enchant

# determining the values of the parameters
string1 = "abc"
string2 = "aef"

# the Levenshtein distance between
# string1 and string2
print(enchant.utils.levenshtein(string1, string2))
