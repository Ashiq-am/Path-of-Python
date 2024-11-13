# Genes are like messages in human
# body which transfers from parent to
# child. Same thing we have used here
# to show the real implementation of
# above concept in python.

class Genes:
    # Inner class
    class Trait:
        walk = 'Fast'
        hair = 'Black'
        disease = ('Diabetes', 'Migraine', 'TB')


class child(Genes):
    # Inner class
    class Trait(Genes.Trait):
        walk = 'Fast'
        hair = 'Black'
        disease = ('Typhoid',) + Genes.Trait.disease


# Driver's code
print(Genes.Trait.disease)
print(child.Trait.disease)
