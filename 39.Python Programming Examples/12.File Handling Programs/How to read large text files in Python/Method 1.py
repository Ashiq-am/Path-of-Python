# import module
import fileinput
import time

# time at the start of program is noted
start = time.time()

# keeps a track of number of lines in the file
count = 0
for lines in fileinput.input(['sample.txt']):
    print(lines)
    count = count + 1

# time at the end of program execution is noted
end = time.time()

# total time taken to print the file
print("Execution time in seconds: ", (end - start))
print("No. of lines printed: ", count)
