# Program to replace text in a file
import os
x = input("Enter text that will replace the existing text:")
f = open("file.txt", "r+")
f1 = open("new.txt", "r+")

f1.write(x)
os.remove("file.txt")
os.rename("new.txt", "file.txt")
f1.close()

print("File replaced")
