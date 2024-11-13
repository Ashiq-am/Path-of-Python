import hashlib
message = "Hello, World!"
hashed = hashlib.sha256(message.encode()).hexdigest()
print(hashed)
