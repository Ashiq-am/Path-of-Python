# function to obtain no
# of topics both alice and
# bob like
def commontopics(alice, bob):
    # initiate count with 0
    count = 0

    # iterating through alice
    for i in range(0, len(alice)):

        # comparing with corresponding
        # bob entry
        if alice[i] == bob[i]:
            # counting similar entries
            count += 1

    # printing the count
    print(count)


# main function
def main():
    commontopics("010101", "101101")
    commontopics("111111", "000000")
    commontopics("110000", "110011")


# driver code
if __name__ == "__main__":
    main()
