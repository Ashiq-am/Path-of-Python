# Python program to explain shutil.unregister_archive_format() method

# importing shutil module
import shutil

# Get the list of
# supported archive formats
formats = shutil.get_archive_formats()

# Print the list
print("Supported archive formats:")
print(formats, "\n")

# Remove an archive format
name = "bztar"
shutil.unregister_archive_format(name)
print("'% s' archive format unregistered successfully." % name, "\n")

# Get the list of
# supported archive formats
formats = shutil.get_archive_formats()

# Print the list
print("Supported archive formats:")
print(formats, "\n")
