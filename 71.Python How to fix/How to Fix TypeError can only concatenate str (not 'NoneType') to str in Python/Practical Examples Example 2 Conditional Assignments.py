status = "active" if user_id == 1 else None
# Fix by converting None to empty string
status = status or ""
message = "User status: " + status
print(message)
