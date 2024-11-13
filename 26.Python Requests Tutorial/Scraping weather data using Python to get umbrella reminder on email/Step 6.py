# Every day at 06:00AM time umbrellaReminder() is called.
schedule.every().day.at("06:00").do(umbrellaReminder)

while True:
	schedule.run_pending()
