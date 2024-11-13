# Python implementation to
# read last N lines of a file
# through Exponential search

# Function to read
# last N lines of the file
def LastNlines(fname, N):
    # assert statement check
    # a condition
    assert N >= 0

    # declaring variable
    # to implement
    # exponential search
    pos = N + 1

    # list to store
    # last N lines
    lines = []

    # opening file using with() method
    # so that file get closed
    # after completing work
    with open(fname) as f:

        # loop which runs
        # until size of list
        # becomes equal to N
        while len(lines) <= N:

            # try block
            try:
                # moving cursor from
                # left side to
                # pos line from end
                f.seek(-pos, 2)

            # exception block
            # to hadle any run
            # time error
            except IOError:
                f.seek(0)
                break

            # finally block
            # to add lines
            # to list after
            # each iteration
            finally:
                lines = list(f)

            # increasing value
            # of variable
            # exponentially
            pos *= 2

    # returning the
    # whole list
    # which stores last
    # N lines
    return lines[-N:]


# Driver Code:
if __name__ == '__main__':
    fname = 'File1.txt'
    N = 3
    try:
        lines = LastNlines(fname, N)
        for line in lines:
            print(line, end='')
    except:
        print('File not found')
