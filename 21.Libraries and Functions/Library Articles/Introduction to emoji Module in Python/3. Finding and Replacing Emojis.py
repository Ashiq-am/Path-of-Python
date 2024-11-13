import emoji

text = "Good morning!  Have a great day! ?"

no_emoji_text = emoji.replace_emoji(text, replace="*")
print(no_emoji_text)
