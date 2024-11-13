"""Concatenation of tuple is the process of joining of two or more Tuples.
Concatenation is done by the use of ‘+’ operator.
Concatenation of tuples is done always from the end of the original tuple.
Other arithmetic operations do not apply on Tuples.
Note- Only same datatypes can be combined with concatenation, an error arises if a list and a tuple are combined."""




# Concatenaton of tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('Geeks', 'For', 'Geeks')

Tuple3 = Tuple1 + Tuple2

# Printing first Tuple
print("Tuple 1: ")
print(Tuple1)

# Printing Second Tuple
print("\nTuple2: ")
print(Tuple2)

# Printing Final Tuple
print("\nTuples after Concatenaton: ")
print(Tuple3)
