import emoji

# A string with emojis
emoji_message = "We will eat some ? and ? tonight!"

# Replace emojis with text
text_message = emoji.demojize(emoji_message)

# Print the text version
print(text_message)
