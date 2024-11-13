# Python code explaining
# SymPy.Polyhedron.faces()

# importing SymPy libraries
from sympy.combinatorics import Permutation, Cycle
from sympy.combinatorics.polyhedron import tetrahedron, octahedron

# Using from
# sympy.combinatorics.polyhedron.Polyhedron.faces()

# Creating Polyhedron
a = tetrahedron.copy()

print ("Polyhedron - faces form : ", a.faces)

a.rotate(0)
print ("\nPolyhedron - faces form : ", a.faces)
