def test_area(self):
    # testing the method Square.area().

    sq = Square(2)  # creates a Square of side 2 units.

    # test if the area of the above square is 4 units,
    # display an error message if it's not.

    self.assertEqual(sq.area(), 4,
                     f'Area is shown {sq.area()} for side = {sq.side} units')
