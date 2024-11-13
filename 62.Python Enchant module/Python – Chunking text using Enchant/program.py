# import the required modules
from enchant.tokenize import get_tokenizer
from enchant.tokenize import HTMLChunker

# the text to be tokenized
text = "<div> <h1> Geeks for Geeks </h1> <br> </div>"

# getting tokenizer class
tokenizer = get_tokenizer("en_US")

# printing tokens without chunking
print("Printing tokens without chunking:")
token_list = []
for words in tokenizer(text):
	token_list.append(words)
print(token_list)


# getting tokenizer class with chunk
tokenizer_chunk = get_tokenizer("en_US", chunkers = (HTMLChunker, ))

# printing tokens after chunking
print("\nPrinting tokens after chunking:")
token_list_chunk = []
for words in tokenizer_chunk(text):
	token_list_chunk.append(words)
print(token_list_chunk)
