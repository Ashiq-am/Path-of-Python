import numpy as np


# defining the display funcrion
def GFG(arr, prec):
    np.set_printoptions(suppress=True, precision=prec)
    print(arr)


if __name__ == "__main__":
    # defining the numpy array with float values
    arr = np.array([123.456, 0.123456, 987.123])

    # displaying the original array
    print("Original Numpy Array : ")
    print(arr, "\n")

    # Converting the array to desired format and then displaying it
    print("Numpy Array without without scientific notation : ")
    GFG(arr, 3)
