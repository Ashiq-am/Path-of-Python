# Module Regular Expression is imported using __import__().
import re

# compile() creates regular expression character class [a-e],
# which is equivalent to [abcde].
# class [abcde] will match with string with 'a', 'b', 'c', 'd', 'e'.
p = re.compile('[a-e]')

# findall() searches for the Regular Expression and return a list upon finding
print(p.findall("Aye, said Mr. Gibenson Stark"))




'''Understanding the Output:
First occurrence is ‘e’ in “Aye” and not ‘A’, as it being Case Sensitive.
Next Occurrence is ‘a’ in “said”, then ‘d’ in “said”, followed by ‘b’ and ‘e’ in “Gibenson”, the Last ‘a’ 
matches with “Stark”.

'''






"""Set class [\s,.] will match any whitespace character, ‘,’, or,’.’ """





import re

# \d is equivalent to [0-9].
p = re.compile('\d')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

# \d+ will match a group on [0-9], group of one or greater size
p = re.compile('\d+')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))















import re

# \w is equivalent to [a-zA-Z0-9_].
p = re.compile('\w')
print(p.findall("He said * in some_lang."))

# \w+ matches to group of alphanumeric character.
p = re.compile('\w+')
print(p.findall("I went to him at 11 A.M., he said *** in some_language."))

# \W matches to non alphanumeric characters.
p = re.compile('\W')
print(p.findall("he said *** in some_language."))















import re

# '*' replaces the no. of occurrence of a character.
p = re.compile('ab*')
print(p.findall("ababbaabbb"))






'''Understanding the Output:
Our RE is ab*, which ‘a’ accompanied by any no. of ‘b’s, starting from 0.
Output ‘ab’, is valid because of singe ‘a’ accompanied by single ‘b’.
Output ‘abb’, is valid because of singe ‘a’ accompanied by 2 ‘b’.
Output ‘a’, is valid because of singe ‘a’ accompanied by 0 ‘b’.
Output ‘abbb’, is valid because of singe ‘a’ accompanied by 3 ‘b’.'''
