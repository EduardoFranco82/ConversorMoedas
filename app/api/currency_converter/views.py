from fastapi import APIRouter, status
from starlette.exceptions import HTTPException
from app.common.exceptions import InvalidCurrencyValue
from app.services.currency_converter import CurrencyAmount

router = APIRouter()

@router.get('/{to_currency}/{from_currency}/{amount}', status_code=200)
def get_currency_amount(
        to_currency: str,
        from_currency: str,
        amount: float
        ):
    
    try:
        currency_amount =  CurrencyAmount.get_currency_amount(to_currency,from_currency, amount)
        return currency_amount

    except InvalidCurrencyValue as currency_value:

        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=currency_value.message)
