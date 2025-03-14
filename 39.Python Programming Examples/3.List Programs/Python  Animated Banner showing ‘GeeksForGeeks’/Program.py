import os
import time

# You can change the width of the display according to your wish.
WIDTH = 250

# Written below currently is GeeksForGeeks. If you wish to get more
# written, you have to add each alphabet manually.
message = "geeksforgeeks".upper()

# The message will get printed here.
printedMessage = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ]

"""
What we have done here is a dictionary mapping the letters to their line.
These mapped indexes identify itself to each letter in the dictionary and
also for each line in the display.
"""
characters = {" ": [" ",
                    " ",
                    " ",
                    " ",
                    " ",
                    " ",
                    " "],

              "E": ["*****",
                    "* ",
                    "* ",
                    "*****",
                    "* ",
                    "* ",
                    "*****"],

              "O": ["*****",
                    "* *",
                    "* *",
                    "* *",
                    "* *",
                    "* *",
                    "*****"],

              "K": [" * *",
                    " * * ",
                    " * * ",
                    " ** ",
                    " * * ",
                    " * * ",
                    " * *"],

              "S": [" **** ",
                    " *	 ",
                    " *	 ",
                    " *** ",
                    "	 * ",
                    "	 * ",
                    " **** "],

              "G": [" *** ",
                    "* * ",
                    "*	 ",
                    "* *** ",
                    "* * ",
                    "* * ",
                    " *** "],

              "F": ["***** ",
                    "*	 ",
                    "*	 ",
                    "**** ",
                    "*	 ",
                    "*	 ",
                    "*	 "],

              "R": [" **** ",
                    " * * ",
                    " * * ",
                    " **** ",
                    " * * ",
                    " * * ",
                    " * * "]

              }

for row in range(7):
    for char in message:
        printedMessage[row] += (str(characters[char][row]) + " ")

offset = WIDTH
while True:
    os.system("cls")

    for row in range(7):
        print(" " * offset + printedMessage[row][max(0, offset * -1):WIDTH - offset])

    offset -= 1

    if offset <= ((len(message) + 2) * 6) * -1:
        offset = WIDTH

    # Use this to change the speed of the animation that you wish to keep.
    time.sleep(0.10)
