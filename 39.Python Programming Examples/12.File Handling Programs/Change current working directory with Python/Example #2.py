# Python program to change the
# current working directory


# importing all necessary libraries
import sys, os

# initial directory
cwd = os.getcwd()

# some non existing directory
fd = 'false_dir/temp'

# trying to insert to flase directory
try:
    print("Inserting inside-", os.getcwd())
    os.chdir(fd)

# Caching the exception
except:
    print("Something wrong with specified directory. Exception- ")
    print(sys.exc_info())

# handling with finally
finally:
    print()
    print("Restoring the path")
    os.chdir(cwd)
    print("Current directory is-", os.getcwd())
