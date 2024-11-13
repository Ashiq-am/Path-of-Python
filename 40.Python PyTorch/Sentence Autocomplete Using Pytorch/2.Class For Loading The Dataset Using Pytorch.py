class TextDataset(torch.utils.data.Dataset):
	def __init__(self, args):
		self.args = args
		self.words = self.load_words()
		self.unique_words = self.get_unique_words()

		self.index_to_word = {index: word for index,\
							word in enumerate(self.unique_words)}
		self.word_to_index = {word: index for index, \
							word in enumerate(self.unique_words)}

		self.word_indexes = [self.word_to_index[w] for w in self.words]

	def load_words(self):
		train_df = pd.read_csv('/content/output.csv')
		text = train_df['Text'].str.cat(sep=' ')
		return text.split(' ')

	def get_unique_words(self):
		word_counts = Counter(self.words)
		return sorted(word_counts, key=word_counts.get, reverse=True)

	def __len__(self):
		return len(self.word_indexes) - self.args

	def __getitem__(self, index):
		return (
			torch.tensor(self.word_indexes[index:index + self.args]),
			torch.tensor(self.word_indexes[index + 1:index + self.args+ 1])
		)
