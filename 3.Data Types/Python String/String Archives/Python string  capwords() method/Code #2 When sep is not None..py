# imports string module
import string

sentence = 'Python is one of the best programming languages.'

# sep parameter is 'g'
formatted = string.capwords(sentence, sep = 'g')
print('When sep = "g"', formatted)

# sep parameter is 'o'
formatted = string.capwords(sentence, sep = 'o')
print('When sep = "o"', formatted)
