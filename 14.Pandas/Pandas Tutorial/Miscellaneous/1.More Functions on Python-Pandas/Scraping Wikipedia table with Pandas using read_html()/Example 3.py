my_table = pd.read_html('https://en.wikipedia.org/wiki/\
Demographics_of_India',
match='Population distribution by states/union territories')
my_table[0].head()
