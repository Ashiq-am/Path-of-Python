# import the module
import tweepy

# assign the values accordingly
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)

# calling the api
api = tweepy.API(auth)

# list of status IDs to be fetched
id_ = [1266978261701210112, 1266735261012111360, 1266342841648898049]

# fetching the statuses
statuses = api.statuses_lookup(id_)

# printing the statuses
for status in statuses:
	print("The status " + str(status.id) + " is posted by " + status.user.screen_name)
	print("This status says : \n\n" + status.text, end = "\n\n")
