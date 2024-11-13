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

# the ID of the list
list_id = ''

# fetching all the lists
statuses = api.list_timeline(list_id = list_id)

# counting the number of statuses fetched
print("The number of statuses fetched from the list are : " + str(len(statuses)))
