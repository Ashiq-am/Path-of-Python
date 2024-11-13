# python3 code to search and
# replace line with other line in file
import fileinput

filename = "GFG.txt"

with fileinput.FileInput(filename,
                         inplace=True, backup='.bak') as f:
    for line in f:
        if "search this line and change it\n" == line:
            print("changing the matched line with this line",
                  end='\n')
        else:
            print(line, end='')
