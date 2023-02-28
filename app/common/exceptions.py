class InvalidCurrencyValue(Exception):
    def __init__(self):
        self.message = 'Invalid Currency Value'
        super().__init__(self.message)