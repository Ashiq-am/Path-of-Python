# get names from the list
for name in filenames:
    # finding the index where
    # the last "." occurs
    k = name.rfind(".")

    # printing the filename
    print(name[:k])
