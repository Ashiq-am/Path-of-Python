with open(one_attachment, 'rb') as f:
	file = MIMEApplication(
		f.read(), name=os.path.basename(one_attachment)
	)
	file['Content-Disposition'] = f'attachment; \
	filename="{os.path.basename(one_attachment)}"'
	msg.attach(file)
