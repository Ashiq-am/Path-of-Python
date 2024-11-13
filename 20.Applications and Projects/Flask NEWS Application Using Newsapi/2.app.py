# this function returns a JSON object
top_headlines = newsapi.get_top_headlines(country="in", language="en")
total_results = top_headlines['totalResults']

# the maximum value for page_size parameter is 100
# so we need to keep it at max 100
if total_results > 100:
	total_results = 100

# fetch articles where no. of articles=total_results
# this returns a list of articles
all_headlines = newsapi.get_top_headlines(country="in",
										language="en",
										page_size=total_results)['articles']
