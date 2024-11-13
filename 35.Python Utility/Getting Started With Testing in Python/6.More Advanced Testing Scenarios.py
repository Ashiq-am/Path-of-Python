import unittest


class TestSumDifferentPatterns(unittest.TestCase):
    def test_list_tuple_values(self):
        # Summation of numbers present
        # in a tuple value
        data = (10 * 2, 200 * 2)
        result = sum(data)
        self.assertEqual(result, 600)

    def test_bad_data_type(self):
        data = "alpha value passed instead of numeric"
        # Because of the below condition, TypeError
        # occurs and hence it will not proceed
        # to next step
        with self.assertRaises(TypeError):
            result = sum(data)


if __name__ == '__main__':
    unittest.main()
