# import required module
import unidecode

# assign string
stringList = ["hell°", "tromsø", "stävänger", "ölut"]

# display orginal string
print('\nOriginal List of Strings:\n', stringList)

for i in range(len(stringList)):
	# remove ascents
	stringList[i] = unidecode.unidecode(stringList[i])

# display new string
print('\nNew List of Strings:\n', stringList)
