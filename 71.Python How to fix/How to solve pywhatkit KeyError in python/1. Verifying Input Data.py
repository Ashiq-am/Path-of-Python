import pywhatkit as kit
try:
  phone_no = "+1234567890"
  message = "This is a text msg"
  if not (phone_no and message):
    raise KeyError("Phone number or message is missing")
  kit.sendwhatmsg(phone_no, message, 15,30)
except KeyError as e:
  print(f"KeyError occurred: {e}")
