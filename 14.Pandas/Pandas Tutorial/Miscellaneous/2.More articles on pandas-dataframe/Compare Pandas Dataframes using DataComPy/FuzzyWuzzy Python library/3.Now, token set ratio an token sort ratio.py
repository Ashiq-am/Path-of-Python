''


"""


# Token Sort Ratio 
fuzz.token_sort_ratio("geeks for geeks", "for geeks geeks") 
100

# This gives 100 as every word is same, irrespective of the position 

# Token Set Ratio 
fuzz.token_sort_ratio("geeks for geeks", "geeks for for geeks") 
88
fuzz.token_set_ratio("geeks for geeks", "geeks for for geeks") 
100
# Score comes 100 in second case because token_set_ratio 
considers duplicate words as a single word. 


"""