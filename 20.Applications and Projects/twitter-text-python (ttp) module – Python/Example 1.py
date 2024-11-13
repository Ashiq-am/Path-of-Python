# import the twitter-text-python module
from ttp import ttp

# the text to be parsed
tweet_text = ("@twitter Sample tweet containing different components." +
			"# gfg # tweeple Visit : https://twitter.com @TwitterIndia")

# instantiating the Parser
p = ttp.Parser()

# parsing the text
result = p.parse(tweet_text)

# printing the username of the
# account being replied to
print("The username being replied to is : " + result.reply)

# printing all the usernames
# mentioned in the tweet
print("\nAll the usernames mentioned are : " + str(result.users))

# printing all the hashtags
# mentioned in the tweet
print("\nAll the hashtags mentioned are : " + str(result.tags))

# printing all the URLs
# mentioned in the tweet
print("\nAll the URLs mentioned are : " + str(result.urls))

# adding hyperlinks to usernames,
# hashtags and URLs
print(result.html)
