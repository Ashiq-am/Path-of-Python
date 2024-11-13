keywords = Trending_topics.suggestions(
keyword='Cloud Computing')
df = pd.DataFrame(keywords)
df.drop(columns= 'mid')
