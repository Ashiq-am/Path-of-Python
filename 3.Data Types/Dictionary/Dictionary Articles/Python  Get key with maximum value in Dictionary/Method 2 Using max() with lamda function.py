# Python code to find key with Maximum value in Dictionary

# Dictionary Initialization
Tv = {'BreakingBad':100, 'GameOfThrones':1292, 'TMKUC' : 88}

Keymax = max(Tv, key= lambda x: Tv[x])
print(Keymax)
