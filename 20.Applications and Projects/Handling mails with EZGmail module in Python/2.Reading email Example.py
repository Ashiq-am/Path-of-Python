import ezgmail

# unread emails
unread = ezgmail.unread()

print("Summary: "+str(ezgmail.summary(unread)))
print("The first thread in the list: " + str(unread[0]))
print("The first message in the first thread: " + str(unread[0].messages[0]))

# attributes of the first message
message = unread[0].messages[0]

# subject
print("subject: "+str(message.subject))

# body
print("body: "+str(message.body))

# sender
print("sender: "+str(message.sender))

# timestamp
print("timestamp: "+str(message.timestamp))

# recent emails
recent = ezgmail.recent(maxResults=10)
print("List of recent threads: " + str(recent))
