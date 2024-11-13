import Levenshtein

modify = Levenshtein.editops("kitten", "sitting")
print(f"The edit operations between 'kitten' and 'sitting' is : {modify}")
