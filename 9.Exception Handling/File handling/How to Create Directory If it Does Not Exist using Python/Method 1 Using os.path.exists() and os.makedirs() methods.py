import os

# checking if the directory demo_folder
# exist or not.
if not os.path.exists("path/to/demo_folder"):
    # if the demo_folder directory is not present
    # then create it.
    os.makedirs("path/to/demo_folder")
