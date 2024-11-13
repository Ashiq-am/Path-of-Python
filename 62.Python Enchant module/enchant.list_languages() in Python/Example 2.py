# import the enchant module
import enchant

for lang in enchant.list_languages():
	if enchant.dict_exists(lang):
		print("The dictionary for " + lang + " exists.")
	else:
		print("The dictionary for " + lang + " does not exists.")
