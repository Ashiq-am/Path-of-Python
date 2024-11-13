from unittest import TestCase

from test import CurrencyConverter

class TestCurrencyConverter(TestCase):
	def test_euro(self):
		self.currency = CurrencyConverter()
		self.assertEqual(self.currency.euro(100), 86)

		def test_yen(self):
			self.currency = CurrencyConverter()
			self.assertEqual(self.currency.yen(100), 10460)

			def test_pound(self):
				self.currency = CurrencyConverter()
				self.assertEqual(self.currency.pound(100), 70)
