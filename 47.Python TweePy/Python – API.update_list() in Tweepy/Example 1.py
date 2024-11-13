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

# the screen name of the owner of the list
owner_screen_name = ""

# the ID of the list
list_id = print("Before using update_list() method")
print("The name of the list is : " + api.get_list(list_id = list_id).name)

# the new name of the list
new_name = "Modified List"

# updating the list
api.update_list(list_id, name = new_name)

print("After using update_list() method")
print("The name of the list is : " + api.get_list(list_id = list_id).name)
