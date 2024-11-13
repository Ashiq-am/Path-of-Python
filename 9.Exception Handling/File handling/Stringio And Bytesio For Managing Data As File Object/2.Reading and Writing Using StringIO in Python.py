from io import StringIO

# Create a new StringIO object with initial content
text_buffer = StringIO("GeeksforGeeks Content")

# Read from the buffer
read_content = text_buffer.read()
print("Read content:", read_content)

# Write new content to the buffer
text_buffer.write(" Added More Articles")

# Get the updated contents of the buffer as a string
updated_content = text_buffer.getvalue()

# Print the updated content
print("Updated content:", updated_content)
