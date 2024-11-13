def repeat(word, m, n):
    # if number of characters greater than length of word.
    # set number of characters = length of word
    if (m > len(word)):
        m = len(word)

    repeat_word = word[:m]
    result = ""

    for i in range(n):
        result = result + repeat_word
    print(result)


# driver code
repeat("geeks", 2, 3)
