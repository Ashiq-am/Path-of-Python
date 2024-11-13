# Creating a set using string
test_set = set("geEks")

iter_gen = iter(test_set)

while True:
    try:
        # get the next item
        print(next(iter_gen))

        ''' do something with element '''

    except StopIteration:
        # if StopIteration is raised,
        # break from loop
        break
