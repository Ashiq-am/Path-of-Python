# @pytest.mark.<tag_name>
@pytest.mark.area

def test_file1_area():
	sq = app.Square(2)
	assert sq.area() == 4, f"area for side {sq.side} units is {sq.area()}"
