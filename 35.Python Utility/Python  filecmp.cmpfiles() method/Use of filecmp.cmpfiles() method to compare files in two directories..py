# Python program to explain filecmp.cmpfiles() method

# importing filecmp module
import filecmp

# Path of first directory
dir1 = "/home / User / Documents"

# Path of second directory
dir2 = "/home / User / Desktop"

# Common files
common = ["file1.txt", "file2.txt", "file3.txt"]

# Shallow compare the files
# common in both directories
match, mismatch, errors = filecmp.cmpfiles(dir1, dir2, common)

# Print the result of
# shallow comparison
print("Shallow comparison:")
print("Match :", match)
print("Mismatch :", mismatch)
print("Errors :", errors, "\n")

# Compare the
# contents of both files
# (i.e deep comparison)
match, mismatch, errors = filecmp.cmpfiles(dir1, dir2, common,
                                           shallow=False)

# Print the result of
# deep comparison
print("Deep comparison:")
print("Match :", match)
print("Mismatch :", mismatch)
print("Errors :", errors)
