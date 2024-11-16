import numpy as np


# defining the display funcrion
def GFG(arr):
    np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
    print(arr)


if __name__ == "__main__":
    # defining the numpy array with float values
    arr = np.array([123.456789, 0.400123456789, 987.123456789])

    # displaying the original array
    print("Original Numpy Array : ")
    print(arr, "\n")

    # Converting the array to desired format and then displaying it
    print("Numpy Array without scientific notation : ")
    GFG(arr)

