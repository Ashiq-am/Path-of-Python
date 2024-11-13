# Python3 program to count special strings

# Returns true if ch is vowel
def isVowel(ch):
    return (ch == 'a' or ch == 'e' or
            ch == 'i' or ch == 'o' or
            ch == 'u')


# Function to check consonant
def isCons(ch):
    return (ch != 'a' and ch != 'e' and
            ch != 'i' and ch != 'o' and
            ch != 'u')


def countSpecial(str):
    lent = len(str)

    # co[i] is going to store counts
    # of consonants from str[len-1]
    # to str[i].
    # vo[i] is going to store counts
    # of vowels from str[len-1]
    # to str[i].
    co = []
    vo = []

    for i in range(0, lent + 1):
        co.append(0)

    for i in range(0, lent + 1):
        vo.append(0)

    # Counting consonants and vowels
    # from end of string.
    if isCons(str[lent - 1]) == 1:
        co[lent - 1] = 1
    else:
        vo[lent - 1] = 1

    for i in range(lent - 2, -1, -1):

        if isCons(str[i]) == 1:
            co[i] = co[i + 1] + 1
            vo[i] = vo[i + 1]

        else:
            co[i] = co[i + 1]
            vo[i] = vo[i + 1] + 1

    # Now we traverse string from beginning
    ans = 0

    for i in range(lent):

        # If vowel, then count of substrings
        # starting with str[i] is equal to
        # count of consonants after it.
        if isVowel(str[i]):
            ans = ans + co[i + 1]

        # If consonant, then count of
        # substrings starting with str[i]
        # is equal to count of vowels
        # after it.
        else:
            ans = ans + vo[i + 1]

    return ans


# Driver Code
str = "adceba"
print(countSpecial(str))
