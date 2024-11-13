# Python3 program to Check if given words
# appear together in a list of sentence

def check(sentence, words):
    res = [all([k in s for k in words]) for s in sentence]
    return [sentence[i] for i in range(0, len(res)) if res[i]]


# Driver code
sentence = ['python coder', 'geeksforgeeks', 'coder in geeksforgeeks']
words = ['coder', 'geeksforgeeks']
print(check(sentence, words))
