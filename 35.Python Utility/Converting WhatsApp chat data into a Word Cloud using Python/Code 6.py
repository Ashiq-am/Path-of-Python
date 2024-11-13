# importing the modules
import matplotlib.plyplot as mpl
from worcloud import WordCloud,STOPWORDS

# reading the csv file as a DataFrame
df1 = pd.read_csv("new_csv.csv")

# defining the stop words
stopwords = set(STOPWORDS)
words=''.join(df1.Message.astype(str)).lower()

# making the word cloud
wordcloud = WordCloud(stopwords = stopwords,
					min_font_size = 10,
					background_color = 'white',
					width = 800,
					height = 800,
					color_func = random_color_func).generate(words)
