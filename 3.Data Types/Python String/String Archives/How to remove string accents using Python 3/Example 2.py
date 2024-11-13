# import required module
import unidecode

# assign string
string = "stävänger"

# display orginal string
print('\nOriginal String:', string)

# remove ascents
outputString = unidecode.unidecode(string)

# display new string
print('\nNew String:', outputString)
