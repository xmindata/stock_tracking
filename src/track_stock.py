import requests
from urllib.parse import urlencode
import csv
import pandas as pd
import numpy as np

class Stock:
    def __init__(self, symbol, request_range):
        self.symbol = symbol
        self.request_range = request_range

    def run_all(self):
        self.fetch_stock_price()
        self.export_price()
        self.export_fundamental()

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
            print (URL+self.symbol+'/batch?'+urlencode(request_params))

            if resp.status_code != 200:
                # This means something went wrong.
                print (resp.status_code)
                raise ApiError('GET /tasks/{}'.format(resp.status_code))

            iex_quote = resp.json()
            return iex_quote
        except Exception as e:
            print(f'There is an error {e}')

    def export_price(self):
        iex_quote = self.fetch_stock_price()
        filename = self.symbol + '.csv'
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ["date", "high", "low", "volume", "open", "close", "label", "change", "changePercent"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            for daily_quote in iex_quote['chart']:
                writer.writerow(daily_quote)

    def export_fundamental(self):
        iex_quote = self.fetch_stock_price()
        filename = self.symbol + '_fundamental.csv'
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ["symbol", "companyName", "primaryExchange", "avgTotalVolume", "marketCap", "peRatio",
                          "week52High", "week52Low", "ytdChange"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerow(iex_quote['quote'])

BABA= Stock('baba', '2y')
BABA.run_all()
