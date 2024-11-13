# Python code explaining
# SymPy.Polyhedron.array_form()

# importing SymPy libraries
from sympy.combinatorics import Permutation, Cycle
from sympy.combinatorics.polyhedron import tetrahedron, octahedron

# Using from
# sympy.combinatorics.polyhedron.Polyhedron.array_form()

# Creating Polyhedron
a = octahedron.copy()

print ("Polyhedron - array_form form : ", a.array_form)

a.rotate(0)
print ("\nPolyhedron - array_form form : ", a.array_form)
