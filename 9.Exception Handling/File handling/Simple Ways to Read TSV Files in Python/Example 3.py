# Simple Way to Read TSV Files in Python using split
ans = []

# open .tsv file
with open("GeekforGeeks.tsv") as f:
    # Read data line by line
    for line in f:
        # split data by tab
        # store it in list
        l = line.split('\t')

    # append list to ans
    ans.append(l)

# print data line by line
for i in ans:
    print(i)
