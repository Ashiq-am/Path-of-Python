# the ID of the status
id = 1272479136133627905

# fetching the status with extended tweet_mode
status = api.get_status(id, tweet_mode = "extended")

# fetching the full_text attribute
full_text = status.full_text

print("The text of the status is : \n\n" + full_text)
