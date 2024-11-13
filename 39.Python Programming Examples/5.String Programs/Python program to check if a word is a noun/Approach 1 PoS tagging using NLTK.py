# import required modules
import nltk
nltk.download('averaged_perceptron_tagger')

# taking input text as India
text = "India"
ans = nltk.pos_tag()

# ans returns a list of tuple
val = ans[0][1]

# checking if it is a noun or not
if(val == 'NN' or val == 'NNS' or val == 'NNPS' or val == 'NNP'):
	print(text, " is a noun.")
else:
	print(text, " is not a noun.")
