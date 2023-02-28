import unittest
from app.services.currency_converter import CurrencyAmount


class CurrencyConverterTestCase(unittest.TestCase):
     def test_currency_converter(self):
        currency_converter = CurrencyAmount.get_currency_amount('BRL', 'USD', 100)
        
        
        result = {
                    'to': 'BRL',
                    'from': 'USD',
                    'amount': 100,
                    'result': 520.1199
                }
        self.assertEqual(currency_converter, result)