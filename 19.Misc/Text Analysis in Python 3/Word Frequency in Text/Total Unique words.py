def word_stats(word_counts):	 # word_counts = count_words_fast(text)
	num_unique = len(word_counts)
	counts = word_counts.values()
	return (num_unique, counts)
