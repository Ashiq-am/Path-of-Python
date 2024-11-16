# Function to ngram
def get_top_n_gram(corpus, ngram_range, n=None):
	vec = CountVectorizer(ngram_range=ngram_range,
						stop_words='english').fit(corpus)
	bag_of_words = vec.transform(corpus)
	sum_words = bag_of_words.sum(axis=0)
	words_freq = [(word, sum_words[0, idx])
				for word, idx in vec.vocabulary_.items()]
	words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
	return words_freq[:n]

# n2_bigram
n2_bigrams = get_top_n_gram(tw_list['content'], (2, 2), 20)
plt.figure(figsize=(8, 5),
		dpi=600) # Push new figure on stack

sns_plot = sns.barplot(x=1, y=0, data=pd.DataFrame(n2_bigrams))
plt.savefig('bigram.jpg') # Save that figure

# n3_trigram
n3_trigrams = get_top_n_gram(tw_list['content'], (3, 3), 20)

plt.figure(figsize=(8, 5),
		dpi=600) # Push new figure on stack

sns_plot = sns.barplot(x=1, y=0, data=pd.DataFrame(n3_trigrams))
plt.savefig('trigram.jpg') # Save that figure
