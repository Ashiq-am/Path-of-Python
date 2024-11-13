# Python code explaining
# SymPy.Polyhedron.vertices()

# importing SymPy libraries
from sympy.combinatorics import Permutation, Cycle
from sympy.combinatorics.polyhedron import tetrahedron, octahedron

# Using from
# sympy.combinatorics.polyhedron.Polyhedron.vertices()

# Creating Polyhedron
a = tetrahedron.copy()

print ("Polyhedron - vertices form : ", a.vertices)

a.rotate(0)
print ("\nPolyhedron - vertices form : ", a.vertices)
