def destination_language():
	print("Enter the language in which you want to convert \
	: Ex. Hindi , English , etc.")
	print()

	# Input destination language in which the user
	# wants to translate
	to_lang = takecommand()
	while (to_lang == "None"):
		to_lang = takecommand()
	to_lang = to_lang.lower()
	return to_lang

to_lang = destination_language()

# Mapping it with the code
while (to_lang not in dic):
	print("Language in which you are trying to convert\
	is currently not available ,please input some other language")
	print()
	to_lang = destination_language()

to_lang = dic[dic.index(to_lang)+1]
