# Function to show report/statistics of todo list
def report():
    nec()
    try:

        nf = open('done.txt', 'r')
        c = 1

        for line in nf:
            line = line.strip('\n')
            don.update({c: line})
            c = c + 1
        print(
            f'{str(datetime.datetime.today()).split()[0]} Pending : {len(d)} Completed : {len(don)}')

    except:
        print(
            f'{str(datetime.datetime.today()).split()[0]} Pending : {len(d)} Completed : {len(don)}')
