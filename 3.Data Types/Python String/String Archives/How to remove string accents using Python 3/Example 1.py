# import required module
import unidecode

# assign string
string = "orčpžsíáýd"

# display orginal string
print('\nOriginal String:', string)

# remove ascents
outputString = unidecode.unidecode(string)

# display new string
print('\nNew String:', outputString)
