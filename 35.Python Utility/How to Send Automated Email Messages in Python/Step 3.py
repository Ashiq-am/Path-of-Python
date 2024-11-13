msg = MIMEMultipart()
msg['Subject'] = subject
msg.attach(MIMEText(text))
