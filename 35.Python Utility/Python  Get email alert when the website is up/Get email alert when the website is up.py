import smtplib, requests, time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

while(1):
	try:
		# Replace the url for your desired website
		url = "https://www.facebook.com/"

		# Send the get request to the website
		r = requests.get(url)

		# creates SMTP session
		s = smtplib.SMTP("smtp.gmail.com", 587)

		# start TLS for security
		s.starttls()

		# Authentication
		s.login("sender_gmail_id", "sender_password")

		# Instance of MIMEMultipart
		msg = MIMEMultipart("alternative")

		# Write the subject
		msg["Subject"]= url + " is working now."

		msg["From"]="sender_gmail_id"
		msg["To"]="receiver_gmail_id"

		# Plain text body of the mail
		text = url + " is running now."

		# Attach the Plain body with the msg instance
		msg.attach(MIMEText(text, "plain"))

		# HTML body of the mail
		html ="<h2>Your site is running now.</h2><br/><a href ='"+ url + "'>Click here to visit.</a>"

		# Attach the HTML body with the msg instance
		msg.attach(MIMEText(html, "html"))

		# Sending the mail
		s.sendmail("sender_gmail_id", "receiver_gmail_id", msg.as_string())
		s.quit()
		print('sent')
		break
	except:
		print('site is down yet...')
		print('sleeping...')

		# Sleeping for 60 seconds. We can change this interval.
		time.sleep(60)
		print('Trying again')
		continue
