# deleting all the lines that are
# not having the minimum length
# excluding the newline '\n' character

# let the min_len = 7
try:
	with open('months.txt', 'r') as fr:
		lines = fr.readlines()

		min_len = 7

		with open('months_4.txt', 'w') as fw:
			for line in lines:
				if len(line.strip('\n')) >= min_len:
					fw.write(line)

	print("Deleted")
except:
	print("Oops! someting error")
