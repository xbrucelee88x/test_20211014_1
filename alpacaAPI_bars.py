
#https://github.com/alpacahq/alpaca-trade-api-python

from alpaca_trade_api.rest import REST
api = REST()

api.get_bars("AAPL", TimeFrame.Hour, "2021-06-08", "2021-06-08", adjustment='raw').df

#Installing using pip

$ pip3 install alpaca-trade-api

#Bars Quotes Trades

##Bars
#option 1: wait for the data
from alpaca_trade_api.rest import REST
api = REST()
api.get_bars("AAPL", TimeFrame.Hour, "2021-06-08", "2021-06-08", adjustment='raw').df

#option 2: iterate over bars

def process_bar(bar):
    # process bar
    print(bar)

bar_iter = api.get_bars_iter("AAPL", TimeFrame.Hour, "2021-06-08", "2021-06-08", adjustment='raw')
for bar in bar_iter:
    process_bar(bar)

#Alternatively, you can decide on your custom timeframes by using the TimeFrame constructor:

from alpaca_trade_api.rest import REST, TimeFrame, TimeFrameUnit

api = REST()
api.get_bars("AAPL", TimeFrame(45, TimeFrameUnit.Minute), "2021-06-08", "2021-06-08", adjustment='raw').df

#Quotes
#option 1: wait for the data

from alpaca_trade_api.rest import REST
api = REST()

api.get_quotes("AAPL", "2021-06-08", "2021-06-08", limit=10).df

option 2: iterate over quotes

def process_quote(quote):
    # process quote
    print(quote)

quote_iter = api.get_quotes_iter("AAPL", "2021-06-08", "2021-06-08", limit=10)
for quote in quote_iter:
    process_quote(quote)
Trades
option 1: wait for the data

from alpaca_trade_api.rest import REST
api = REST()

api.get_trades("AAPL", "2021-06-08", "2021-06-08", limit=10).df

option 2: iterate over trades

def process_trade(trade):
    # process trade
    print(trade)

trades_iter = api.get_trades_iter("AAPL", "2021-06-08", "2021-06-08", limit=10)
for trade in trades_iter:
    process_trade(trade)
There are 2 streams available as described here.
The free plan is using the iex stream, while the paid subscription is using the sip stream.
You could subscribe to bars, trades or quotes and trade updates as well.
Under the example folder you could find different code samples to achieve different goals. Let's see the basic example
We present a new Streamer class under alpaca_trade_api.stream for API V2.

from alpaca_trade_api.stream import Stream

async def trade_callback(t):
    print('trade', t)


async def quote_callback(q):
    print('quote', q)


# Initiate Class Instance
stream = Stream(<ALPACA_API_KEY>,
                <ALPACA_SECRET_KEY>,
                base_url=URL('https://paper-api.alpaca.markets'),
                data_feed='iex')  # <- replace to SIP if you have PRO subscription

# subscribing to event


#sing submit_order()
#Below is an example of submitting a bracket order.

api.submit_order(
    symbol='SPY',
    side='buy',
    type='market',
    qty='100',
    time_in_force='day',
    order_class='bracket',
    take_profit=dict(
        limit_price='305.0',
    ),
    stop_loss=dict(
        stop_price='295.5',
        limit_price='295.5',
    )
)
stream.subscribe_trades(trade_callback, 'AAPL')
stream.subscribe_quotes(quote_callback, 'IBM')

stream.run()
    
    
    
    
    
    
