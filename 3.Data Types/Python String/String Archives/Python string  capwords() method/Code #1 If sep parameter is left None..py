# imports string module
import string

sentence = 'Python is one of the best programming languages.'

# sep parameter is left None
formatted = string.capwords(sentence, sep = None)

print(formatted)
