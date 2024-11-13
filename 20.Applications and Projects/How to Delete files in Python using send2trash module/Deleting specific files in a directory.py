import os
import send2trash

# walking through the directory
for folder, subfolders, files in os.walk('/Users/tithighosh/Documents'):

    for file in files:

        # checking if file is
        # of .txt type
        if file.endswith('.txt'):
            path = os.path.join(folder, file)

            # printing the path of the file
            # to be deleted
            print('deleted : ', path)

            # deleting the file
            send2trash.send2trash(path)
