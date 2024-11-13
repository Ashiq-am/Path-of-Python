import os, sys

# It oversees all the file in the folder
# and changes it with a proper extension.
for filename in os.listdir(os.path.dirname(os.path.abspath(__file__))):

    base_file, ext = os.path.splitext(filename)


    if ext == "":
        os.rename(filename, base_file + ".jpg")
