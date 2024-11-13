# Tokenization function using spaCy
def tokenize(text):
    return [token.text for token in nlp(text)]

TEXT.tokenize = tokenize # tokenization and remove punctuation
TEXT.build_vocab(train_data, max_size=10000) # Building vocabulary
LABEL.build_vocab(train_data)
# Tokenize and preprocess reviews
tokenized_reviews = [data.Example.fromlist([review.text, None], [('text', TEXT), ('label', None)]) for review in train_data.examples]
all_words = [word for example in tokenized_reviews for word in example.text]
