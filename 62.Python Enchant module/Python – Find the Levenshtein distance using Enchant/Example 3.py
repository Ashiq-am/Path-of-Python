# import the enchant module
import enchant

# determining the values of the parameters
string1 = "Computer Science Portal"
string2 = "Computer Portal"

# the Levenshtein distance between
# string1 and string2
print(enchant.utils.levenshtein(string1, string2))
