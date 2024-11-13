inputstring = 'some strings are present in between "geeks" "for" "geeks" '

""" 
here split() method will split the string for every quotation ( " ) .i.e. 
['some strings are present in between ', 'geeks', ' ', 'for', ' ', 'geeks', ' ']. 

Then we will be storing all the strings at odd index. 

"""

result = inputstring.split('"')[1::2]
print(result);
