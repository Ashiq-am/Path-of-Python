from itertools import chain

# some consonants
consonants = ['d', 'f', 'k', 'l', 'n', 'p']

# some vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# resultatnt list
res = list(chain(consonants, vowels))

# sorting the list
res.sort()

print(res)
