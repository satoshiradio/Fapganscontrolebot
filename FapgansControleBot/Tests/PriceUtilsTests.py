import unittest

from FapgansControleBot.Utils.PriceUtils import price_formatter


class PriceUtilsTests(unittest.TestCase):

    def test_format_simple_price(self):
        price = price_formatter("10")
        self.assertEqual(10, price)

    def test_format_price_with_K(self):
        self.assertEqual(10000, price_formatter("10k"))
        self.assertEqual(20000, price_formatter("20K"))

    def test_format_invalid_price(self):
        with self.assertRaises(ValueError):
            price_formatter("10a")
