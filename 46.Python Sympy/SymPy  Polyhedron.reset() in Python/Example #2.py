# Python code explaining
# SymPy.Polyhedron.reset()

# importing SymPy libraries
from sympy.combinatorics import Permutation, Cycle
from sympy.combinatorics.polyhedron import tetrahedron, octahedron

# Using from
# sympy.combinatorics.polyhedron.Polyhedron.reset()

# Creating Polyhedron
a = octahedron.copy()

print ("Polyhedron - reset form : ", a.reset)

a.rotate(0)
print ("\nPolyhedron - reset form : ", a.reset)
