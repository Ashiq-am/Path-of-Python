# python code to search
# text and replace that text
# in file

import fileinput

filename = "GFG.txt"

with fileinput.FileInput(filename,
                         inplace=True, backup='.bak') as f:
    for line in f:
        if "replace text" in line:
            print(line.replace("replace text",
                               "changed text"), end='')
        else:
            print(line, end='')
