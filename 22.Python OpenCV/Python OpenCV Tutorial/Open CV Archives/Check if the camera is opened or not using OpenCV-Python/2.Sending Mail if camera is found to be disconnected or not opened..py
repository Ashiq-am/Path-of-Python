# Python program to send
# the mail


import smtplib


conn = smtplib.SMTP('smtp.gmail.com', 587)

conn.ehlo()
conn.starttls()

# Enter the sender's details
conn.login('Enter sender \'s gmail address',
		'Enter sender\'s password')

conn.sendmail('Enter sender\'s gmail address',
			'Enter Reciever\'s gmail address',
			'Enter message to be sent')

conn.quit()
