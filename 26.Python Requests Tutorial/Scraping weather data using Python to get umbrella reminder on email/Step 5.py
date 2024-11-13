# start TLS for security
smtp_object.starttls()
# Authentication
smtp_object.login("YOUR EMAIL", "PASSWORD")
subject = "Umbrella Reminder"
body = f"Take an umbrella before leaving the house.\
Weather condition for today is ", {
	sky}, " and temperature is {temperature} in {city}."
msg = f"Subject:{subject}\n\n{body}\n\nRegards,\
\nGeeksforGeeks".encode('utf-8')

# sending the mail
smtp_object.sendmail("FROM EMAIL ADDRESS",
					"TO EMAIL ADDRESS", msg)
# terminating the session
smtp_object.quit()
print("Email Sent!")
