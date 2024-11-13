def repeat(word, m, n):
    # if number of characters greater than length of word.
    # set number of characters = length of word
    if (m > len(word)):
        m = len(word)

    repeat_word = word[:m]
    print(repeat_word * n)


# driver code
repeat("geeks", 2, 3)
