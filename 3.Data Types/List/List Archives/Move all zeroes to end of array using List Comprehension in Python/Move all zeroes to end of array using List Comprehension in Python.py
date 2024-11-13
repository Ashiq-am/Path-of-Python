# Function to append all zeros at the end
# of array
def moveZeros(arr):
    # first expression returns a list of
    # all non zero elements in arr in the
    # same order they were inserted into arr
    # second expression returns a list of
    # zeros present in arr
    return [nonZero for nonZero in arr if nonZero != 0] + \
           [Zero for Zero in arr if Zero == 0]


# Driver function
if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    print(moveZeros(arr))
