# Python Program to find all anagrams of str in
# a list of strings.
from collections import Counter

my_list = ["geeks", "geeg", "keegs", "practice", "aa"]
str = "eegsk"

# use anonymous function to filter anagrams of x.
# Please refer below article for details of reversed
# https://www.geeksforgeeks.org/anagram-checking-python-collections-counter/
result = list(filter(lambda x: (Counter(str) == Counter(x)), my_list))

# printing the result
print(result)
