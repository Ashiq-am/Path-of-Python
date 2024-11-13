import nltk
s = input('Enter the file name which contains a sentence: ')
file1 = open(s)
sentence = file1.read()
file1.close()
p = input('Enter the file name which contains a paragraph: ')
file2 = open(p)
paragraph = file2.read()
file2.close()
