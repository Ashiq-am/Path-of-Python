# Python code explaining
# SymPy.Polyhedron.cyclic_form()

# importing SymPy libraries
from sympy.combinatorics import Permutation, Cycle
from sympy.combinatorics.polyhedron import tetrahedron, octahedron

# Using from
# sympy.combinatorics.polyhedron.Polyhedron.cyclic_form()

# Creating Polyhedron
a = tetrahedron.copy()

print ("Polyhedron - cyclic_form form : ", a.cyclic_form)

a.rotate(0)
print ("\nPolyhedron - cyclic_form form : ", a.cyclic_form)
