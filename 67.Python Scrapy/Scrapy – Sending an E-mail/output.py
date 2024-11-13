# import module
from scrapy.mail import MailSender

# setup mailer
mailer = MailSender(mailfrom="Something@gmail.com",
					smtphost="smtp.gmail.com", smtpport=465, smtppass="MySecretPassword")

# send mail
mailer.send(to=["abc@gmail.com"], subject="Scrapy Mail",
			body="Hi ! GeeksForGeeks", cc=["another@example.com"])
