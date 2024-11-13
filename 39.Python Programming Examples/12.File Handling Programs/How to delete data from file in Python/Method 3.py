# code to delete a particular
# data from a file

# open file in read mode
with open("sample.txt", "r") as f:
    # read data line by line
    data = f.readlines()

# open file in write mode
with open("sample.txt", "w") as f:
    for line in data:

        # condition for data to be deleted
        if line.strip("\n") != "Age : 20":
            f.write(line)
