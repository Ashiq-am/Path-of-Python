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
list_id = 4343

# fetching the list
list = api.get_list(list_id=list_id)

# printing the information
print("The id is : " + str(list.id))
print("The id_str is : " + list.id_str)
print("The name is : " + list.name)
print("The uri is : " + list.uri)
print("The subscriber_count is : " + str(list.subscriber_count))
print("The member_count is : " + str(list.member_count))
print("The mode is : " + list.mode)
print("The slug is : " + list.slug)
print("The full_name is : " + list.full_name)
print("The list was created on : " + str(list.created_at))
print("Is the authenticated user following the list? : " + str(list.following))
print("The screen name of the owner of the list is : " + list.user.screen_name)
