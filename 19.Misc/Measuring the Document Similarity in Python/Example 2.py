# counts frequency of each word
# returns a dictionary which maps
# the words to their frequency.
def count_frequency(word_list):
    D = {}

    for new_word in word_list:

        if new_word in D:
            D[new_word] = D[new_word] + 1

        else:
            D[new_word] = 1

    return D


# returns dictionary of (word, frequency)
# pairs from the previous dictionary.
def word_frequencies_for_file(filename):
    line_list = read_file(filename)
    word_list = get_words_from_line_list(line_list)
    freq_mapping = count_frequency(word_list)

    print("File", filename, ":", )
    print(len(line_list), "lines, ", )
    print(len(word_list), "words, ", )
    print(len(freq_mapping), "distinct words")

    return freq_mapping
