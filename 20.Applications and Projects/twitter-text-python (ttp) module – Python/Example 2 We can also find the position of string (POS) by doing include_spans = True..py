# import the twitter-text-python module
from ttp import ttp

# the text to be parsed
tweet_text = ("@twitter Sample tweet containing different components." +
			"# gfg # tweeple Visit : https://twitter.com @TwitterIndia")

# instantiating the Parser
# with spans
p = ttp.Parser(include_spans = True)

# parsing the text
result = p.parse(tweet_text)

# printing all the usernames
# mentioned in the tweet with POS
print("All the usernames mentioned are : " + str(result.users))

# printing all the hashtags
# mentioned in the tweet with POS
print("\nAll the hashtags mentioned are : " + str(result.tags))

# printing all the URLs
# mentioned in the tweet with POS
print("\nAll the URLs mentioned are : " + str(result.urls))
