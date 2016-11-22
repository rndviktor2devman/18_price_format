import unittest
from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):
    def test_failure_type_none(self):
        price = None
        with self.assertRaises(TypeError):
            format_price(price)

    def test_failure_type_string(self):
        price = 'abcde'
        with self.assertRaises(ValueError):
            format_price(price)

    def test_success_str_int_4digit(self):
        price = '1234'
        price_formatted = '1 234'
        self.assertEqual(format_price(price), price_formatted)

    def test_success_str_4_removes_zeroes(self):
        price = '1234.00'
        price_formatted = '1 234'
        self.assertEqual(format_price(price), price_formatted)

    def test_success_str_8_removes_zeroes(self):
        price = '12345678.00'
        price_formatted = '12 345 678'
        self.assertEqual(format_price(price), price_formatted)

    def test_success_str_4_removes_more_zeroes(self):
        price = '1234.00000'
        price_formatted = '1 234'
        self.assertEqual(format_price(price), price_formatted)

    def test_success_str_8_removes_more_zeroes(self):
        price = '12345678.00000'
        price_formatted = '12 345 678'
        self.assertEqual(format_price(price), price_formatted)

    def test_success_str_4_adds_missing_zero(self):
        price = '1234.1'
        price_formatted = '1 234.10'
        self.assertEqual(format_price(price), price_formatted)

    def test_success_str_8_adds_missing_zero(self):
        price = '12345678.1'
        price_formatted = '12 345 678.10'
        self.assertEqual(format_price(price), price_formatted)

    def test_success_str_4_removes_more_digits(self):
        price = '1234.12345'
        price_formatted = '1 234.12'
        self.assertEqual(format_price(price), price_formatted)

    def test_success_str_8_removes_more_digits(self):
        price = '12345678.12345'
        price_formatted = '12 345 678.12'
        self.assertEqual(format_price(price), price_formatted)

    def test_success_round(self):
        price = '12345678.12565'
        price_formatted = '12 345 678.13'
        self.assertEqual(format_price(price), price_formatted)


if __name__ == '__main__':
    unittest.main()
