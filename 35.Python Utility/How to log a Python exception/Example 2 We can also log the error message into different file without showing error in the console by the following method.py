# importing the module
import logging

try:
    printf("GeeksforGeeks")
except Exception as Argument:

    # creating/opening a file
    f = open("demofile2.txt", "a")

    # writing in the file
    f.write(str(Argument))

    # closing the file
    f.close()
