updater = Updater("your_own_API_Token got from BotFather",
				use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Enter the text you want to show to the user whenever they start the bot")
