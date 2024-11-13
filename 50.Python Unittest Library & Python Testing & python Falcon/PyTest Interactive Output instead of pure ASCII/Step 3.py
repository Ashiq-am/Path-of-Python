import maths

def test_calc_addition():
	output = maths.calc_addition(2, 4)
	assert output == 6

def test_calc_substraction():
	output = maths.calc_substraction(2, 4)
	assert output == -2

def test_calc_multiply():
	output = maths.calc_multiply(2, 4)
	assert output == 8

def test_area():
	output = maths.area_of_rectangle(2, 5)
	assert output == 11

def test_perimeter():
	output = maths.perimeter_of_rectangle(2, 5)
	assert output == 14
