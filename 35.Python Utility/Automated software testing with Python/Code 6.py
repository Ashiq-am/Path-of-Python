from .. import app

def test_file1_area():
	sq = app.Square(2)
	assert sq.area() == 4, f"area for side {sq.side} units is {sq.area()}"

def test_file1_perimeter():
	sq = app.Square(-1)
	assert sq.perimeter() == -1, f'perimeter is shown {sq.perimeter()} rather than -1'
