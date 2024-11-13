# Python 3 program to check if all
# array are same or not
def areSame(a, n):
    m = {i: 0 for i in range(len(a))}

    # hash map to store the frequency
    # of every element

    for i in range(n):
        m[a[i]] += 1

    if (len(m) == 1):
        return True
    else:
        return False


# Driver code
if __name__ == '__main__':
    arr = [1, 2, 3, 2]

    n = len(arr)

    if (areSame(arr, n)):
        print("All Elements are Same")
    else:
        print("Not all Elements are Same")
