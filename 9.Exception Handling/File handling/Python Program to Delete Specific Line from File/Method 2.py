# deleting a line on the basis
# of a matching text (exactly)

# we want to remove a line
# with text = '8-August'
try:
    with open('months.txt', 'r') as fr:
        lines = fr.readlines()

        with open('months_2.txt', 'w') as fw:
            for line in lines:

                # strip() is used to remove '\n'
                # present at the end of each line
                if line.strip('\n') != '8-August':
                    fw.write(line)
    print("Deleted")
except:
    print("Oops! someting error")
