#Setting initial value of the counter to zero
rowcount = 0
#iterating through the whole file
for row in open("Data.csv"):
    # printing the result
    rowcount+= 1
    print("Number of lines present:-", rowcount)
