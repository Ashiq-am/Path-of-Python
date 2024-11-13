import magic

# printing the human readable type of the file
print(magic.from_file('apple.jpg'))

# printing the mime type of the file
print(magic.from_file('apple.jpg', mime = True))
