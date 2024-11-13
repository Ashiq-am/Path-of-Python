# Python code explaining
# SymPy.Polyhedron.size()

# importing SymPy libraries
from sympy.combinatorics import Permutation, Cycle
from sympy.combinatorics.polyhedron import tetrahedron, octahedron

# Using from
# sympy.combinatorics.polyhedron.Polyhedron.size()

# Creating Polyhedron
a = octahedron.copy()

print ("Polyhedron - size form : ", a.size)

a.rotate(0)
print ("\nPolyhedron - size form : ", a.size)
