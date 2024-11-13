# the text to be tweeted
status = "This is a tweet is a reply."

# the ID of the tweet to be replied to
in_reply_to_status_id = ""

# posting the tweet
api.update_status(status, in_reply_to_status_id)
