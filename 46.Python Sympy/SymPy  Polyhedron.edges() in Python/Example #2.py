# Python code explaining
# SymPy.Polyhedron.edges()

# importing SymPy libraries
from sympy.combinatorics import Permutation, Cycle
from sympy.combinatorics.polyhedron import tetrahedron, octahedron

# Using from
# sympy.combinatorics.polyhedron.Polyhedron.edges()

# Creating Polyhedron
a = octahedron.copy()

print ("Polyhedron - edges form : ", a.edges)

a.rotate(0)
print ("\nPolyhedron - edges form : ", a.edges)
