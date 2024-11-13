# import the module
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

# the text to be transliterated
text = "Suprabhaata"

# printing the transliterated text
print(transliterate(text, sanscript.IAST, sanscript.GUJARATI))
