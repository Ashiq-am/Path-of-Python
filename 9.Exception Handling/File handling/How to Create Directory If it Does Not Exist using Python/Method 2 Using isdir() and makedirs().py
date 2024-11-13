import os

# checking if the directory demo_folder2
# exist or not.
if not os.path.isdir("path/to/demo_folder2"):
    # if the demo_folder2 directory is
    # not present then create it.
    os.makedirs("path/to/demo_folder2")
