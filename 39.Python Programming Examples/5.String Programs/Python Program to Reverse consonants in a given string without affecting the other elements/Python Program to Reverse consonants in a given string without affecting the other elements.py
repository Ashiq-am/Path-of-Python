# Function to check element is consonant or not
def isConsonant(i):
    vow = ['a', 'e', 'i', 'o', 'u']

    # if not vowel return true
    if i not in vow:
        return True
    return False


def reverseConsonant(s):
    # convert string into list
    s = list(s)

    # storing consonants in a list
    cons = []
    for i in s:
        if isConsonant(i):
            cons.append(i)
    k = len(cons) - 1

    # Replace the consonants with the
    # element present in consonant list
    # from last.
    for i in range(len(s)):
        if isConsonant(s[i]):
            s[i] = cons[k]
            k -= 1
    return "".join(s)


print(reverseConsonant("hello world"))
print(reverseConsonant("bcdfghjklm"))
