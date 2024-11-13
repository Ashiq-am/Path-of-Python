# Program to send message
# on Instagram using Python.

# importing Bot form instabot library.
from instabot import Bot

# Creating bot varible.
bot = Bot()

# Login using bot.
bot.login(username="Your_username",
		password="Your_password")

# Make a list of followers/friends
urer_ids = ["username1", "username2", "....."]

# Message
text = "I like GFG"

# Sending messages
bot.send_messages(text, urer_ids)
