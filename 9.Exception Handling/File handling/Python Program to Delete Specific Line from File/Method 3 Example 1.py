# deleting a line matching
# a specific pattern or
# containing a specific string

# we want to delete a line
# containing string = 'ber'
try:
    with open('months.txt', 'r') as fr:
        lines = fr.readlines()

        with open('months_3.txt', 'w') as fw:
            for line in lines:

                # find() returns -1
                # if no match found
                if line.find('ber') == -1:
                    fw.write(line)
    print("Deleted")
except:
    print("Oops! someting error")
