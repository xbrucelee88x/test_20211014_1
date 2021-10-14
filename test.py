
#https://github.com/alpacahq/alpaca-trade-api-python

from alpaca_trade_api.rest import REST
api = REST()

api.get_bars("AAPL", TimeFrame.Hour, "2021-06-08", "2021-06-08", adjustment='raw').df

