'''test_algebra.py'''

import mathfuncs

def test_square():
	assert mathfuncs.Algebra.square(40) == 1600
	assert mathfuncs.Algebra.square(5) == 25

def test_cube():
	assert mathfuncs.Algebra.cube(40) == 64000
	assert mathfuncs.Algebra.cube(5) == 125
