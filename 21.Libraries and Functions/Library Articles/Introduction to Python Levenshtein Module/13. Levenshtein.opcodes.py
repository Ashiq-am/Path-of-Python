import Levenshtein

list_op = Levenshtein.opcodes("apple", "mapple")
print(f"The opcodes between 'apple' and 'mapple' is : {list_op}")
