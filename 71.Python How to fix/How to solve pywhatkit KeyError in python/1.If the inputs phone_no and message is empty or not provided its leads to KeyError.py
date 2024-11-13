import pywhatkit as kit
try:
    phone_no = ""
    message = ""
    if not (phone_no and message):
        raise KeyError("phone_no or message is missing")
    kit.sendwhatmsg(phone_no, message,15,10)
except KeyError as e:
    print(f"KeyError occurred: {e}")
