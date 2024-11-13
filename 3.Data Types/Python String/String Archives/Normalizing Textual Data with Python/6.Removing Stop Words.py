# download stpwords
import nltk

nltk.download('stopwords')

# import nltk for stopwords
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
print(stop_words)

# assign string
no_wspace_string = 'python released in was a major revision of the language that is not completely backward compatible and much python code does not run unmodified on python with python s endoflife only python x and later are supported with older versions still supporting eg windows and old installers not restricted to bit windows'

# convert string to list of words
lst_string = [no_wspace_string][0].split()
print(lst_string)

# remove stopwords
no_stpwords_string = ""
for i in lst_string:
    if not i in stop_words:
        no_stpwords_string += i + ' '

# removing last space
no_stpwords_string = no_stpwords_string[:-1]
print(no_stpwords_string)
