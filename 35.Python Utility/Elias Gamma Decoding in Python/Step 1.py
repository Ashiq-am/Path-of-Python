# define the function
def Elias_Gamma_Decoding(x):
    # convert to list
    x = list(x)

    # initialize k to 0
    K = 0
    while True:

        # check if k is not 0 in through
        # list index
        if not x[K] == '0':
            break

        # increment k value
        K = K + 1
