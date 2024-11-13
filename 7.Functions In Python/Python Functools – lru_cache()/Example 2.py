from functools import lru_cache


@lru_cache(maxsize=100)
def count_vowels(sentence):
    sentence = sentence.casefold()
    return sum(sentence.count(vowel) for vowel in 'aeiou')


print(count_vowels("Welcome to Geeksforgeeks"))
