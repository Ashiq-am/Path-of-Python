# Python program to explain shutil.unregister_unpack_format() method

# importing shutil module
import shutil

# Get the list of
# supported unpack formats
formats = shutil.get_unpack_formats()

# Print the list
print("Supported unpack formats:")
print(formats, "\n")

# Remove an unpack format
name = "gztar"
shutil.unregister_unpack_format(name)
print("%s unpack format unregistered successfully." % name, "\n")

# Get the list of
# supported unpack formats
formats = shutil.get_unpack_formats()

# Print the list
print("Supported unpack formats:")
print(formats, "\n")
