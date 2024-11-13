import shutil
import os

# Create a file
with open("my_file.txt", "w") as file:
    file.write("Hello, world!")

# Move and rename the file
shutil.move("my_file.txt", "new_directory/my_new_file.txt")

# Verify the new file location and name
print(os.listdir("new_directory"))
