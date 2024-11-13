import pandas as pd
import matplotlib.plyplot as mpl
from worcloud import WordCloud, STOPWORDS

df = pd.read_csv(r"WhatsAppChat.txt",
				header = None,
				error_bad_lines = False,
				encoding = 'utf8')
df = df.drop(0)
df.columns = ['Date', 'Convo']
Chat = df["Convo"].str.split("-", n = 1,
							expand = True)
df['Time'] = Chat[0]
df['Content'] = Chat[1]
Chat1 = df["Content"].str.split(": ", n = 1,
								expand=True)
df['User'] = Chat1[0]
df['Message'] = Chat1[1]
df = df.drop(columns = ['Convo'])
df['Message'] = df['Message'].str.lower()
df['Message'] = df['Message'].str.replace('< media omitted >', 'Media Shared')
df['Message'] = df['Message'].str.replace('this message was deleted', 'DeletedMsg')
df.to_csv("new_csv.csv", index = False)

def random_color_func(word = None,
					font_size = None,
					position = None,
					orientation = None,
					font_path = None,
					random_state = None):
	h = int(360.0 * 21.0 / 255.0)
	s = int(100.0 * 255.0 / 255.0)
	l = int(100.0 * float(random_state.randint(60, 120)) / 255.0)

df1 = pd.read_csv("new_csv.csv")
stopwords = set(STOPWORDS)
words = ''.join(df1.Message.astype(str)).lower()

wordcloud = WordCloud(stopwords = stopwords,
					min_font_size = 10,
					background_color = 'white',
					width = 800,
					height = 800,
					color_func = random_color_func).generate(words)

mpl.figure(figsize = (8, 8), facecolor = None)
mpl.imshow(wordcloud, interpolation = "bilinear")
mpl.axis("off")
mpl.tight_layout(pad = 0)
mpl.show()
