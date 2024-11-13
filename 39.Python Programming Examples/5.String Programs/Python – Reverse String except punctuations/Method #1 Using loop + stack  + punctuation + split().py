# Python3 code to demonstrate working of
# Reverse String except punctuations
# Using loop + stack + punctuation + split()
from string import punctuation

# initializing string
test_str = 'geeks# for&%% gee)ks'

# printing original string
print("The original string is : " + str(test_str))

# getting punctuations
punc_set = set(punctuation)
res = []
for sub in test_str.split(' '):

    # getting all aphabets
    alphas = [chr for chr in sub if chr not in punc_set]
    for chr in sub:

        # checking for punctuations
        if chr not in punc_set:
            res.append(alphas.pop())
            continue
        else:
            res.append(chr)

        # handling spaces
    res.append(' ')
res = "".join(res)

# printing result
print("The Reversed String ignoring punctuation : " + str(res))
