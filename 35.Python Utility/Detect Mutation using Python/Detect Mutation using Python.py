# import random library
import random


# function to generate dna strands
def generateDNASequence():
    # list of available DNA bases
    l = ['C', 'A', 'G', 'T']
    res = ""
    for i in range(0, 40):
        # creating the DNA strand by appending
        # random characters from the list
        res = res + random.choice(l)
    return res


# function to alter dna strands
def applyGammaRadiation(dna):
    # possibility of mutation is generated randomly
    pos = random.randint(1, 100)
    cdna = ''

    # list of available DNA bases
    l = ['C', 'A', 'G', 'T']

    # if the possibility of mutation generated randomly
    # is >50 then mutation happens
    if (pos > 50):

        # the position where mutation will take place
        # is chosen randomly
        changepos = random.randint(0, 39)
        dl = []

        # the characters in DNA strand is converted to list
        dl[:0] = dna

        # the character at the determined mutation position
        # is fetched.
        ch = "" + dl[changepos]

        # since the fetched character should be different from
        # the one replacing it we remove the fetched character
        # from the list of available choices for choosing another
        # character in its place
        l.remove(ch)

        # the new character or DNA base is chosen from the list
        ms = random.choice(l)
        cl = []

        # DNA strand characters are again appended to a new list
        cl[:0] = dna

        # the new base in the mutated position is set
        cl[changepos] = ms

        # the characters in the cl list is converted to string again
        # this is the new mutated DNA string
        cdna = ''.join([str(e) for e in cl])

    # if possibility of mutation is less than 50% then no
    # mutation happens
    else:

        # if no mutation occurs original dna is same as mutated dna
        cdna = dna
    return cdna


# function to detect mutation
def detectMutation(dna, cdna):
    count = 0

    # x and y take each character in dna and cdna
    # for character by character comparison
    for x, y in zip(dna, cdna):

        # if the character at the same index match
        # then the count is increased
        if x == y:
            count = count + 1

        # incase of mismatch the loop is broken
        else:
            break

    # the count value points to the index before the
    # position of mutation
    return count


dna = generateDNASequence()
print(dna + " (Original DNA)")
cdna = applyGammaRadiation(dna)
print(cdna + " (DNA after radiation)")
count = detectMutation(dna, cdna)

# if count=40 it means all the characters of the 2 strands match
# hence no mutation
if count == 40:
    print("No Mutation detected")

# if count is less than 40
# it means mutation has occurred
else:

    # ^ denotes the position of mutation
    pos = "^"
    print(pos.rjust(count + 1))
    print("Mutation detected at pos = ", (count + 1))
