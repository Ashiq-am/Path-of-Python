# import the enchant module
import enchant

# create dictionary for the language
# in use(en_US here)
dict = enchant.Dict("en_US")

# list of words
words = ["cmputr", "watr", "study", "wrte"]

# find those words that may be misspelled
misspelled =[]
for word in words:
	if dict.check(word) == False:
		misspelled.append(word)
print("The misspelled words are : " + str(misspelled))

# suggest the correct spelling of
# the misspelled words
for word in misspelled:
	print("Suggestion for " + word + " : " + str(dict.suggest(word)))
