from io import StringIO

# Create a StringIO object
string_io = StringIO()

# Write to the in-memory "file"
string_io.write("Hello, ")
string_io.write("world!")

# Get the value as a string
result_string = string_io.getvalue()

# Close the StringIO object (optional, but good practice)
string_io.close()

print(result_string)
