# screen name of the account to be fetched
screen_name = "geeksforgeeks"

# number of statuses to be fetched
count = 3

# fetching the retweets
statuses = api.retweets_of_me(count = count)

print(str(len(statuses)) + " number of statuses have been retweeted.")
