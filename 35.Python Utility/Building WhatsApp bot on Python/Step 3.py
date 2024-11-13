from twilio.twiml.messaging_response import MessagingResponse

response = MessagingResponse()
msg = response.message()
msg.body('this is the response/reply from the bot')
