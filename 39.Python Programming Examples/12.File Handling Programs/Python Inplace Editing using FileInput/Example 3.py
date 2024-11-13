# python3 code to search text in
# line and replace that line with
# other line in file
import fileinput

filename = "GFG.txt"

with fileinput.FileInput(filename,
						inplace = True, backup ='.bak') as f:
	for line in f:
		if "searchtext" in line:
			print("changing this line with line that contains searched text",
				end ='\n')
		else:
			print(line, end ='')
