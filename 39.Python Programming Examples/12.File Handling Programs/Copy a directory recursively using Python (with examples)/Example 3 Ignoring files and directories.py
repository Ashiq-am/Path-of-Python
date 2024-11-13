# Python program to demonstrate
# shutil.copytree()


# imporing modules
import shutil


# Declaring the ignore function
def ignoreFunc(file):
    def _ignore_(path, names):
        # List containing names of file
        # that are needed to ignore
        ignored = []

        # check if file in names
        # then add it to list
        if file in names:
            ignored.append(file)
        return set(ignored)

    return _ignore_


# Source path
src = 'D:/Pycharm projects /GeeksforGeeks/src'

# Destination path
dest = 'D:/Pycharm projects/GeeksforGeeks/dst'

# Copying the contents from Source
# to Destination without some
# specified files or directories
shutil.copytree(src, dest, ignore=ignoreFunc('a'))
