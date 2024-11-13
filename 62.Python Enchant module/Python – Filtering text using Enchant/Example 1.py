# import the required modules
from enchant.tokenize import get_tokenizer
from enchant.tokenize import EmailFilter

# the text to be tokenized
text = "The email is abc@gmail.com"

# getting tokenizer class
tokenizer = get_tokenizer("en_US")

# printing tokens without filtering
print("Printing tokens without filtering:")
token_list = []
for words in tokenizer(text):
	token_list.append(words)
print(token_list)

# getting tokenizer class with filter
tokenizer_filter = get_tokenizer("en_US", [EmailFilter])

# printing tokens after filtering
print("\nPrinting tokens after filtering:")
token_list_filter = []
for words in tokenizer_filter(text):
	token_list_filter.append(words)
print(token_list_filter)
