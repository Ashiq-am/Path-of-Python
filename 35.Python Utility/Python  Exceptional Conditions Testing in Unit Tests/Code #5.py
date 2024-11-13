class TestConversion(unittest.TestCase):
	def test_bad_int(self):
		self.assertRaisesRegex(
				ValueError, 'invalid literal .*',
				parse_int, 'N/A')
