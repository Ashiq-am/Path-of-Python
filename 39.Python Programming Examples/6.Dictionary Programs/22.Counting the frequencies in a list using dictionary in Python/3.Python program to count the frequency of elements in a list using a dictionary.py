# Python program to count the frequency of
# elements in a list using a dictionary

def CountFrequency(my_list):
    # Creating an empty dictionary
    count = {}

    for i in [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]:
        count[i] = count.get(i, 0) + 1
    return count

# Driver function
if __name__ == "__main__":
    my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
    print(CountFrequency(my_list))
