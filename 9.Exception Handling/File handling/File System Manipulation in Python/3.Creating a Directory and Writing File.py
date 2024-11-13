import os

# Create a directory
os.mkdir("my_directory")

# Change to the new directory
os.chdir("my_directory")

# Create a file and write to it
with open("my_file.txt", "w") as file:
    file.write("Hello, world!")

# Verify the file and its content
print(os.listdir())
# Output: ['my_file.txt']
