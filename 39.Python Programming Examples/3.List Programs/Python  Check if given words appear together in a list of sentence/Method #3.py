# Python3 program to Check if given words
# appear together in a list of sentence

def check(sentence, words):
    res = list(map(lambda x: all(map(lambda y: y in x.split(),
                                     words)), sentence))
    return [sentence[i] for i in range(0, len(res)) if res[i]]


# Driver code
sentence = ['python coder', 'geeksforgeeks', 'coder in geeksforgeeks']
words = ['coder', 'geeksforgeeks']
print(check(sentence, words))
