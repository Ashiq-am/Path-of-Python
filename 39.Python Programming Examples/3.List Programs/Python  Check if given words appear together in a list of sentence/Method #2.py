# Python3 program to Check if given words
# appear together in a list of sentence

def check(sentence, words):
    res = []
    for substring in sentence:
        k = [w for w in words if w in substring]
        if (len(k) == len(words)):
            res.append(substring)

    return res


# Driver code
sentence = ['python coder', 'geeksforgeeks', 'coder in geeksforgeeks']
words = ['coder', 'geeksforgeeks']
print(check(sentence, words))
