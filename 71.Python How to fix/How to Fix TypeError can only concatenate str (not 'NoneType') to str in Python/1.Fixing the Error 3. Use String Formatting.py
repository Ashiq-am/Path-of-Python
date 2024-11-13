# Using format()
message = "{}{}".format(greeting, title if title is not None else "No Title Provided")
print(message)
# Using f-strings (Python 3.6+)
message = f"{greeting}{title if title is not None else 'No Title Provided'}"
print(message)
