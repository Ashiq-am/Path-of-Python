# ID of the recipient
recipient_id = ''

# text to be sent
text = "This is a Direct Message."

# the ID of the media
attachment_media_id = ''

# sending the direct message
direct_messages = api.send_direct_message(recipient_id, text,
					attachment_media_id = attachment_media_id)
