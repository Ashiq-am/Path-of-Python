# import the torch and torchtext dataset packages.
import torch
import torchtext

# access the dataset in torchtext package
# using .datasets followed by dataset name.
text_data = torchtext.datasets.IMDB(split='train')

# define a function to tokenize
# the words in the corpus
def tokenize(label, line):
	return line.split()


# define a empty list to store
# the tokenized words
tokens = []

# iterate over the text_data and
# tokenize each line and store
# it in the list tokens
for label, line in text_data:
	tokens += tokenize(label, line)

print('The total no. of tokens in imdb dataset is',
	len(tokens))
