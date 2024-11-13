# Python3 program to print Horizontal
# filling

def horizontalFill(records, tape, nt):
    # It is used for checking whether
    # tape is full or not
    sum = 0
    # It is used for calculating
    # total retrieval time
    Retrieval_Time = 0

    # It is used for calculating
    # mean retrieval time
    current = 0

    # vector is used because n number of
    # records can insert in one tape with
    # size constraint
    v = []

    for i in range(nt):

        # Null vector obtained to use fresh
        # vector 'v'
        v.clear()
        Retrieval_Time = 0

        # initialize variables to
        # 0 for each iteration
        sum = 0
        print("tape", i + 1, ": [ ", end="")

        # sum is used for checking whether
        # i'th tape is full or not
        sum += records[current]

        # check sum less than size of tape
        while (sum <= tape[i]):
            print(records[current], end=" ")
            v.append(records[current])

            # increment in j for next record
            current += 1
            sum += records[current]

        print("]", end="")

        # calculating total retrieval
        # time
        for i in range(len(v)):
            # MRT formula
            Retrieval_Time += v[i] * (len(v) - i)

            # calculating mean retrieval time
        # using formula
        Mrt = Retrieval_Time / len(v)

        # v.size() is function of vector is used
        # to get size of vector
        print("tMRT :", Mrt)

    # Driver Code


if __name__ == "__main__":
    records = [15, 2, 8, 23, 45, 50, 60, 120]
    tape = [25, 80, 160]

    # store the size of records[]
    n = len(records)

    # store the size of tapes[]
    m = len(tape)
    # sorting of an array is required to
    # attain greedy approach of
    # algorithm
    records.sort()
    horizontalFill(records, tape, m)