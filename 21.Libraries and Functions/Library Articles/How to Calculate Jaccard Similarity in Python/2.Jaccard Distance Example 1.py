def jaccard_distance(set1, set2):
    # Symmetric difference of two sets
    Symmetric_difference = set1.symmetric_difference(set2)
    # Unions of two sets
    union = set1.union(set2)

    return len(Symmetric_difference) / len(union)


set_a = {"Geeks", "for", "Geeks", "NLP", "DSc"}
set_b = {"Geek", "for", "Geeks", "DSc.", 'ML', "DSA"}

distance = jaccard_distance(set_a, set_b)
print("Jaccard distance:", distance)
