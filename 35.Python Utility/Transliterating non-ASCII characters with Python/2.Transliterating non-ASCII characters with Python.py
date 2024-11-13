# Create devanagari transliteration dictionary
devanagari_translit_dict = {
	'\u0905': 'A', '\u0906': 'AA', '\u0907': 'I', '\u0908': 'II',
	'\u0909': 'U', '\u090A': 'UU', '\u090F': 'E', '\u0910': 'AI',
	'\u0913': 'O', '\u0914': 'AU', '\u0915': 'K', '\u0916': 'KH',
	'\u0917': 'G', '\u0918': 'GH', '\u0919': 'NG', '\u091A': 'C',
	'\u091B': 'CH', '\u091C': 'J', '\u091D': 'JH', '\u091E': 'NY',
	'\u091F': 'TT', '\u0920': 'TTH', '\u0921': 'DD', '\u0922': 'DDH',
	'\u0923': 'NN', '\u0924': 'T', '\u0925': 'TH', '\u0926': 'D',
	'\u0927': 'DH', '\u0928': 'N', '\u092A': 'P', '\u092B': 'PH',
	'\u092C': 'B', '\u092D': 'BH', '\u092E': 'M', '\u092F': 'Y',
	'\u0930': 'R', '\u0932': 'L', '\u0933': 'LL', '\u0935': 'V',
	'\u0936': 'SH', '\u0937': 'SS', '\u0938': 'S', '\u0939': 'H',
	'\u093E': 'AA', '\u093F': 'I', '\u0940': 'II', '\u0941': 'U',
	'\u0942': 'UU', '\u0947': 'E', '\u0948': 'AI', '\u094B': 'O',
	'\u094C': 'AU', '\u094D': '', '\u0902': 'n'}

# Define function transliterating text
def transliterate(text, translit_dict):
	new_word = ''
	for letter in text:
		new_letter = ''
		if letter in translit_dict:
			new_letter = translit_dict[letter]
		else:
			new_letter = letter
		new_word += new_letter
	return new_word

# Input text in devanagari
text = "आप नीचे अपनी भाषा और इनपुट उपकरण चुनें और लिखना आरंभ करें"

# Obtain Transliterated text for given input text
transliterated_text = transliterate(text, devanagari_translit_dict)
print(transliterated_text)
