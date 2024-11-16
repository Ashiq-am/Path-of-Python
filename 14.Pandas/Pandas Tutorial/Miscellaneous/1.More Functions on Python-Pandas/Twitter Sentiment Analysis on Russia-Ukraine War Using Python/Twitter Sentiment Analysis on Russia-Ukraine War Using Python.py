# Import Libraries

from textblob import TextBlob
import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk
import re
import string
import seaborn as sns


from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer


# The dataset consists of tweets from
# total 8 hashtags and present in
# separated csv files. All those csv files are loaded.
tweets=pd.read_csv("/dataset/Russia_invade.csv")
tweets=tweets.append(pd.read_csv("/Russian_border_Ukraine.csv"))
tweets=tweets.append(pd.read_csv("/Russian_troops.csv"))
tweets=tweets.append(pd.read_csv("/StandWithUkraine.csv"))
tweets=tweets.append(pd.read_csv("/Ukraine_border.csv"))
tweets=tweets.append(pd.read_csv("/Ukraine_nato.csv"))
tweets=tweets.append(pd.read_csv("/Ukraine_troops.csv"))
tweets=tweets.append(pd.read_csv("/Ukraine_war.csv"))


tweets.drop_duplicates(inplace=True) # remove duplicates


# slicing the date , and removing the time portion
tweets['date'] = tweets.date.str.slice(0, 10)
# checking all the unique dates in the dataset
print(tweets['date'].unique())

# checking how many unique language
# tweets are present in the dataset
print(tweets["lang"].unique())
# Removing RT, Punctuation etc
def remove_rt(x): return re.sub('RT @\w+: ', " ", x)

def rt(x): return re.sub(
	"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", x)

tweets["content"] = tweets.content.map(remove_rt).map(rt)
tweets["content"] = tweets.content.str.lower()
tweets[['polarity', 'subjectivity']] = tweets['content'].apply(
    lambda Text: pd.Series(TextBlob(Text).sentiment))

for index, row in tweets['content'].iteritems():
    score = SentimentIntensityAnalyzer().polarity_scores(row)
    neg = score['neg']
    neu = score['neu']
    pos = score['pos']
    comp = score['compound']

    if neg > pos:
        tweets.loc[index, 'sentiment'] = "negative"
    elif pos > neg:
        tweets.loc[index, 'sentiment'] = "positive"
    else:
        tweets.loc[index, 'sentiment'] = "neutral"

    tweets.loc[index, 'neg'] = neg
    tweets.loc[index, 'neu'] = neu
    tweets.loc[index, 'pos'] = pos
    tweets.loc[index, 'compound'] = comp
tweets[["content", "sentiment", "polarity",
		"subjectivity", "neg", "neu", "pos"]].head(5)
total_pos = len(tweets.loc[tweets['sentiment'] == "positive"])
total_neg = len(tweets.loc[tweets['sentiment'] == "negative"])
total_neu = len(tweets.loc[tweets['sentiment'] == "neutral"])
total_tweets = len(tweets)
print("Total Positive Tweets % : {:.2f}"
	.format((total_pos/total_tweets)*100))
print("Total Negative Tweets % : {:.2f}"
	.format((total_neg/total_tweets)*100))
print("Total Neutral Tweets % : {:.2f}"
	.format((total_neu/total_tweets)*100))
mylabels = ["Positive", "Negative", "Neutral"]
mycolors = ["Green", "Red", "Blue"]

plt.figure(figsize=(8, 5),
		dpi=600) # Push new figure on stack
myexplode = [0, 0.2, 0]
plt.pie([total_pos, total_neg, total_neu], colors=mycolors,
		labels=mylabels, explode=myexplode)
plt.show()
pos_list = []
neg_list = []
neu_list = []
for i in tweets["date"].unique():
	temp = tweets[tweets["date"] == i]
	positive_temp = temp[temp["sentiment"] == "positive"]
	negative_temp = temp[temp["sentiment"] == "negative"]
	neutral_temp = temp[temp["sentiment"] == "neutral"]
	pos_list.append(((positive_temp.shape[0]/temp.shape[0])*100, i))
	neg_list.append(((negative_temp.shape[0]/temp.shape[0])*100, i))
	neu_list.append(((neutral_temp.shape[0]/temp.shape[0])*100, i))

neu_list = sorted(neu_list, key=lambda x: x[1])
pos_list = sorted(pos_list, key=lambda x: x[1])
neg_list = sorted(neg_list, key=lambda x: x[1])

x_cord_neg = []
y_cord_neg = []

x_cord_pos = []
y_cord_pos = []

x_cord_neu = []
y_cord_neu = []

for i in neg_list:
	x_cord_neg.append(i[0])
	y_cord_neg.append(i[1])


for i in pos_list:
	x_cord_pos.append(i[0])
	y_cord_pos.append(i[1])

for i in neu_list:
	x_cord_neu.append(i[0])
	y_cord_neu.append(i[1])


plt.figure(figsize=(16, 9),
		dpi=600) # Push new figure on stack
plt.plot(y_cord_neg, x_cord_neg, label="negative",
		color="red")
plt.plot(y_cord_pos, x_cord_pos, label="positive",
		color="green")
plt.plot(y_cord_neu, x_cord_neu, label="neutral",
		color="blue")
plt.xticks(np.arange(0, len(tweets["date"].unique()) + 1, 5))
plt.xticks(rotation=90)
plt.grid(axis='x')

plt.legend()
# Removing Punctuation
def remove_punct(text):
	text = "".join([char for char in text if
					char not in string.punctuation])
	text = re.sub('[0-9]+', '', text)
	return text


tw_list['punct'] = tw_list['content'].apply(
lambda x: remove_punct(x))

# Appliyng tokenization
def tokenization(text):
	text = re.split('\W+', text)
	return text


tw_list['tokenized'] = tw_list['punct'].apply(
	lambda x: tokenization(x.lower()))

# Removing stopwords
stopword = nltk.corpus.stopwords.words('english')

def remove_stopwords(text):
	text = [word for word in text if
			word not in stopword]
	return text

tw_list['nonstop'] = tw_list['tokenized'].apply(
lambda x: remove_stopwords(x))

# Appliyng Stemmer
ps = nltk.PorterStemmer()

def stemming(text):
	text = [ps.stem(word) for word in text]
	return text

tw_list['stemmed'] = tw_list['nonstop'].apply(
lambda x: stemming(x))

tw_list.head()
# Appliyng Countvectorizer
countVectorizer = CountVectorizer(analyzer=clean_text)
countVector = countVectorizer.fit_transform(tw_list['content'])
count_vect_df = pd.DataFrame(
	countVector.toarray(),
columns=countVectorizer.get_feature_names())
count_vect_df.head()

# Most Used Words
count = pd.DataFrame(count_vect_df.sum())
countdf = count.sort_values(0,
							ascending=False).head(20)
countdf[1:11]
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

