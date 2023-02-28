import requests
from app.common.exceptions import InvalidCurrencyValue
from decimal import Decimal
from app.config import settings


class CurrencyAmount:
    
    def get_currency_amount(to_currency: str, from_currency: str, amount: float)->dict:
        
        currency_values = ('USD','BRL','EUR','BTC','ETH')
        
        if to_currency in currency_values and from_currency in currency_values:
            pass
        else:
        
            raise InvalidCurrencyValue
        
        
        
        url = f'https://api.apilayer.com/fixer/convert?to={to_currency}&from={from_currency}&amount={amount}'

        headers= {
        "apikey": settings.API_KEY
        }
        response = requests.request("GET", url, headers=headers,)

        if response.status_code == 200:
            
            result = response.json()
            
            
            return  {
                'to': to_currency,
                'from': from_currency,
                'amount': amount,
                'result': result.get('result')
            }
        else:
            response.status_code = 400