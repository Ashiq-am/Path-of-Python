# Python3 program to find an element
# such that sum of right side element
# is equal to sum of left side

# Function to compute partition
def findElement(arr, size):
    # Maintains left cumulative sum
    left_sum = 0

    # Maintains right cumulative sum
    right_sum = 0
    i = 0
    j = -1
    j = size - 1

    while (i < j):
        if (i < j):
            left_sum += arr[i]
            right_sum += arr[j]

            # Keep moving i towards center
            # until left_sum is found
            # lesser than right_sum
            while (left_sum < right_sum and
                   i < j):
                i += 1
                left_sum += arr[i]

            # Keep moving j towards center
            # until right_sum is found
            # lesser than left_sum
            while (right_sum < left_sum and
                   i < j):
                j -= 1
                right_sum += arr[j]
            j -= 1
            i += 1
    if (left_sum == right_sum):
        return arr[i]
    else:
        return -1


# Driver code
if __name__ == '__main__':
    arr = [2, 3, 4,
           1, 4, 5]
    size = len(arr)
    print(findElement(arr, size))

