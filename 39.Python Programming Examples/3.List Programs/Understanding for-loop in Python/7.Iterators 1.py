# Python program to demonstrate
# power of iterators


# creating our own loop
def newForLoop(iterable):
    # extracting iterator out of iterable
    iterator = iter(iterable)

    # condition to check if looping is done
    loopingFinished = False

    while not loopingFinished:
        try:
            nextItem = next(iterator)
        except StopIteration:
            loopingFinished = True
        else:
            print(nextItem)


# Driver's code
newForLoop([1, 2, 3, 4])
