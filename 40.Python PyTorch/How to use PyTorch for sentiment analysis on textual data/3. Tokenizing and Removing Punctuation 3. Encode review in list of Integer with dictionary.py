encoded_reviews = [[word_to_int[word] for word in example.text] for example in tokenized_reviews] # Encoding reviews into lists of integers

# Making encoded reviews of the same length
padded_reviews = pad_sequence([torch.tensor(review) for review in encoded_reviews])

# Pretty-print a subset of the outputs
pprint({
    "Tokenized Reviews": [example.text[:10] for example in tokenized_reviews[:5]],  # Show first 5 reviews, first 10 tokens
    "All Words": all_words[:50],  # Show first 50 words
    "Sorted Words": sorted_words[:50],  # Show first 50 sorted words
    "Word to Integer Dictionary": {k: word_to_int[k] for k in list(word_to_int)[:10]},  # Show first 10 entries
    "Encoded Reviews": encoded_reviews[:5],  # Show first 5 encoded reviews
    "Padded Reviews Shape": padded_reviews.shape  # Show shape of padded_reviews
})
