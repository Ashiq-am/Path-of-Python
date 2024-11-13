import vonage

# Replace with your Vonage API key and secret
api_key = 'your_api_key'
api_secret = 'your_api_secret'

# Create a Vonage client
client = vonage.Client(key=api_key, secret=api_secret)

# Create a Vonage SMS client
sms = vonage.Sms(client)

# Replace with your phone number and the message you want to send
to_number = 'recipient_phone_number'
message = 'This is a message from vonage'

# Send SMS
response = sms.send_message({
	'from': 'Vonage API',
	'to': to_number,
	'text': message
})

# Check the response
if response['messages'][0]['status'] == '0':
	print(
		f"SMS sent successfully to {to_number}. Message ID: {response['messages'][0]['message-id']}")
else:
	print(
		f"Failed to send SMS. Error: {response['messages'][0]['error-text']}")
