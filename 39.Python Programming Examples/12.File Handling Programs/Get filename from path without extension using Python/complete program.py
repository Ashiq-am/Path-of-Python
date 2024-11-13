# import module
import ntpath

# used path style of both the UNIX
# and Windows os to show it works on both.
paths = [
    "E:\Programming Source Codes\Python\sample.py",
    "D:\home\Riot Games\VALORANT\live\VALORANT.exe"]

# empty array to store file basenames
filenames = []

for path in paths:
    # used basename method to get the filename
    filenames.append(ntpath.basename(path))

# get names from the list
for name in filenames:
    # finding the index where
    # the last "." occurs
    k = name.rfind(".")

    # printing the filename
    print(name[:k])
