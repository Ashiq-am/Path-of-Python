''



'''
fuzz.partial_ratio("geeks for geeks", "geeks for geeks!") 
100
# Exclamation mark in second string, 
but still partially words are same so score comes 100

fuzz.partial_ratio("geeks for geeks", "geeks geeks") 
64
# score is less because there is a extra 
token in the middle middle of the string. 


'''