# the ID of the status
ID = 1265569813281280006

# obtaining the status
status = api.get_status(ID)

# printing the text of the status
print("The text of the status is : \n\n" + status.text)

# printing the screen name
print("\nThe status was posted by : " + status.user.screen_name)

# printing the number of likes
print("The status has been liked " + str(status.favorite_count) + " number of times.")

# printing the number of retweets
print("The status has been retweeted " + str(status.retweet_count) + " number of times.")
