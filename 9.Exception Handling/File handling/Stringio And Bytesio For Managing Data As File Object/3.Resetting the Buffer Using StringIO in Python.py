from io import StringIO

# Create a new StringIO object
text_buffer = StringIO()

# Write some text to the buffer
text_buffer.write("Hello, GeeksforGeeks!")

# Get the contents of the buffer as a string
content_before_reset = text_buffer.getvalue()
print("Before reset:", content_before_reset)

# Reset the buffer
text_buffer.seek(0)
text_buffer.truncate()

# Write new content to the buffer
text_buffer.write("I am New Website!")

# Get the updated contents of the buffer as a string
content_after_reset = text_buffer.getvalue()

# Print the updated content
print("After reset:", content_after_reset)
