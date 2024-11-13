# Python code explaining
# SymPy.Polyhedron.rotate()

# importing SymPy libraries
from sympy.combinatorics import Permutation, Cycle
from sympy.combinatorics.polyhedron import tetrahedron, octahedron

# Using from
# sympy.combinatorics.polyhedron.Polyhedron.rotate()

# Creating Polyhedron
a = octahedron.copy()

print ("Polyhedron - rotate form : ", a.array_form)

# Rotating the axis
a.rotate(0)

print ("\nPolyhedron - rotate form : ", a.array_form)
