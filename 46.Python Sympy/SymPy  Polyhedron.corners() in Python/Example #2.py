# Python code explaining
# SymPy.Polyhedron.corners()

# importing SymPy libraries
from sympy.combinatorics import Permutation, Cycle
from sympy.combinatorics.polyhedron import tetrahedron, octahedron

# Using from
# sympy.combinatorics.polyhedron.Polyhedron.corners()

# Creating Polyhedron
a = octahedron.copy()

print ("Polyhedron - corners form : ", a.corners)

a.rotate(0)
print ("\nPolyhedron - corners form : ", a.corners)
