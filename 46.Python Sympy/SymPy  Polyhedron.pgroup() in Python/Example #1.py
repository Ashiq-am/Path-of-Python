# Python code explaining
# SymPy.Polyhedron.pgroup()

# importing SymPy libraries
from sympy.combinatorics import Permutation, Cycle
from sympy.combinatorics.polyhedron import tetrahedron, octahedron

# Using from
# sympy.combinatorics.polyhedron.Polyhedron.pgroup()

# Creating Polyhedron
a = tetrahedron.copy()

print ("Polyhedron - pgroup form : ", a.pgroup)

a.rotate(0)
print ("\nPolyhedron - pgroup form : ", a.pgroup)
