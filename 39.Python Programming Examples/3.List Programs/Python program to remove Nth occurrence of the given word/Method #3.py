# Python3 program to remove Nth
# occurrence of the given word

# Function to remove nth word
def omit(list1, word, n1):
    # for counting the occurence of word
    count = 0

    # for counting the index number
    # where we are at present
    index = 0

    for i in list1:
        index += 1
        if i == word:
            count += 1
            if count == n1:
                # (index-1) because in list
                # indexing start from 0th position
                list1.pop(index - 1)
    return list1


# Driver code
list1 = ["he", "is", "ankit", "is",
         "raj", "is", "ankit raj"]

word = "is"
n1 = 3

print("new list is :", omit(list1, word, n1))
