# Importing sendpdf function
# From pdf_mail Library
from pdf_mail import sendpdf

# Taking input of following values
# ex-"abcd@gmail.com"
sender_email_address = input()

# ex-"xyz@gmail.com"
receiver_email_address = input()

# ex-" abcd1412"
sendere_email_password = input()

# ex-"Heading of email"
subject_of_email = input()

# ex-" Matter to be sent"
body_of_email = input()

# ex-"Name of file"
filename = input()

# ex-"C:/Users / Vasu Gupta/ "
location_of_file = input()


# Create an object of sendpdf function
k = sendpdf(sender_email_address,
			receiver_email_address,
			sender_email_password,
			subject_of_email,
			body_of_email,
			filename,
			location_of_file)

# sending an email
k.email_send()
