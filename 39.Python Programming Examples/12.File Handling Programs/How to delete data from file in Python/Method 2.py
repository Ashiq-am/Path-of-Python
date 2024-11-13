# code to delete entire data
# but not the file, it is in


# open file
f = open("sample.txt", "r+")

# absolute file positioning
f.seek(0)

# to erase all data
f.truncate()
