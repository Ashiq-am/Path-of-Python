from io import BytesIO

# Create a new BytesIO object
binary_buffer = BytesIO()

# Hexadecimal representation of "Hello"
binary_buffer.write(b'\x48\x65\x6C\x6C\x6F')

# Get the contents of the buffer as bytes
result_bytes = binary_buffer.getvalue()

# Print the result
print(result_bytes)
