def gmail_url(update: Update, context: CallbackContext):
	update.message.reply_text("gmail link here")


def youtube_url(update: Update, context: CallbackContext):
	update.message.reply_text("youtube link")


def linkedIn_url(update: Update, context: CallbackContext):
	update.message.reply_text("Your linkedin profile url")


def geeks_url(update: Update, context: CallbackContext):
	update.message.reply_text("GeeksforGeeks url here")


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)


def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)
