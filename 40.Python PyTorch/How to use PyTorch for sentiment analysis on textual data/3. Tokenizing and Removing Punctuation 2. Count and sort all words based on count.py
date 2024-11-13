word_counts = Counter(all_words) # Sorting based on occurrences
sorted_words = sorted(word_counts, key=word_counts.get, reverse=True)
# dictionary for integers
word_to_int = {word: idx + 1 for idx, word in enumerate(sorted_words)}
