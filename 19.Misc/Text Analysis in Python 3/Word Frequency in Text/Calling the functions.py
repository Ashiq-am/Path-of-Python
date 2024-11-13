text = read_book("./Books / English / shakespeare / Romeo and Juliet.txt")

word_counts = count_words_fast(text)
(num_unique, counts) = word_stats(word_counts)
print(num_unique, sum(counts))
