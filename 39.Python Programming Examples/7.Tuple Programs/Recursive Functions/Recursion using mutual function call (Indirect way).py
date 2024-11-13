def recursive(data):

    callDepth = 0


    if (callDepth > MAX_DEPTH):
        return;

    # Increase call depth
    callDepth += 1

    # do other processing
    recursive(data);

    # do other processing
    # Decrease call depth
    callDepth -= 1

# This code is contributed by Pratham76
