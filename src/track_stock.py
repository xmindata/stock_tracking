# fetching daily stock data from IEX
# Needs to fill in the symbol (BABA) and request range (e.g. 1 year)
import requests
from urllib.parse import urlencode
import csv

class Stock:
    def __init__(self, symbol, request_range):
        self.symbol = symbol
        self.request_range = request_range

    def fetch_stock_price(self):
        try:
            request_type = "quote,chart"
            request_last = "10"
            request_token = "Tsk_ff9db2bb5ef84c929272b4a176a9089a"
            URL = "https://sandbox.iexapis.com/stable/stock/"
            request_params = {
                    'types':request_type,
                    'range':self.request_range,
                    'last':request_last,
                    'token':request_token
            }

            resp = requests.get("https://sandbox.iexapis.com/stable/stock/baba/batch?types=quote,chart&range=1m&last=10&token=Tsk_ff9db2bb5ef84c929272b4a176a9089a")
            print (URL+symbol+'/batch?'+urlencode(request_params))


            return iex_quote
        except Exception as e:
            print(f'There is an error {e}')

    def export_price(self):
        pass

    def export_fundamental(self):
        ipass

