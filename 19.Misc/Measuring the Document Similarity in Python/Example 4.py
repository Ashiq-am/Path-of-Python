def documentSimilarity(filename_1, filename_2):
    # filename_1 = sys.argv[1]
    # filename_2 = sys.argv[2]
    sorted_word_list_1 = word_frequencies_for_file(filename_1)
    sorted_word_list_2 = word_frequencies_for_file(filename_2)
    distance = vector_angle(sorted_word_list_1, sorted_word_list_2)

    print("The distance between the documents is: % 0.6f (radians)" % distance)
