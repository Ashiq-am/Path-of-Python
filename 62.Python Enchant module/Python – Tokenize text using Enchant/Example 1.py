# import the module
from enchant.tokenize import get_tokenizer

# the text to be tokenized
text = ("Natural language processing (NLP) is a field " +
	"of computer science, artificial intelligence " +
	"and computational linguistics concerned with " +
	"the interactions between computers and human " +
	"(natural) languages, and, in particular, " +
	"concerned with programming computers to " +
	"fruitfully process large natural language " +
	"corpora. Challenges in natural language " +
	"processing frequently involve natural " +
	"language understanding, natural language" +
	"generation frequently from formal, machine" +
	"-readable logical forms), connecting language " +
	"and machine perception, managing human-" +
	"computer dialog systems, or some combination " +
	"thereof.")

# getting tokenizer class
tokenizer = get_tokenizer("en_US")

token_list =[]
for words in tokenizer(text):
	token_list.append(words)

# print the words with POS
print(token_list)
