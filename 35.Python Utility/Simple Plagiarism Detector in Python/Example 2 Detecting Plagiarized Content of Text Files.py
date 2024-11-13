# importing SequenceMatcher of difflib module
from difflib import SequenceMatcher

with open('doc1.txt') as first_file, open('doc2.txt') as second_file:

    # Reading Both Text Files
    file1 = first_file.read()
    file2 = second_file.read()

    # Comparing Both Text Files
    ab = SequenceMatcher(None, file1,
                         file2).ratio()

    # converting decimal output in integer
    result = int(ab * 100)
    print(f"{result}% Plagiarized Content")
