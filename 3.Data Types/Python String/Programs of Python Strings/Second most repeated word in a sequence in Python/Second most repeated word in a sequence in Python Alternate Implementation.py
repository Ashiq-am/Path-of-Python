# Second most repeated word in a sequence in Python

def secondFrequent(input):
    from collections import Counter

    # this sorts from most common to least common to least common
    c = Counter(input)

    # c.most_common()[1] prints ('bbb',2)
    # c.most_common()[1][0] prints output: bbb
    print(c.most_common()[1][0])


# Driver code
input = ['aaa', 'bbb', 'ccc', 'bbb', 'aaa', 'aaa']
secondFrequent(input)
