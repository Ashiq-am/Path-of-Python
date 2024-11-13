class TestConversion(unittest.TestCase):
	def test_bad_int(self):
		with self.assertRaisesRegex(ValueError, 'invalid literal .*'):
			r = parse_int('N/A')
