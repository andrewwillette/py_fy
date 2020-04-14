from services.alpaca.alpaca import api
import time

def short(ticker):
    # Submit a market order to open a short position of one share
    order = api.submit_order(ticker, 1, 'sell', 'market', 'day')
    print("Market order submitted.")

    # Submit a limit order to attempt to grow our short position
    # First, get an up-to-date price for our symbol
    symbol_bars = api.get_barset(ticker, 'minute', 1).df.iloc[0]
    symbol_price = symbol_bars[ticker]['close']
    print('symbol price is ' + str(symbol_price))
    # Submit an order for one share at that price
    order = api.submit_order(ticker, 1, 'sell', 'limit', 'day', symbol_price)
    print("Limit order submitted.")

    # Wait a second for our orders to fill...
    print('Waiting...')
    time.sleep(1)

    # Check on our position
    position = api.get_position(ticker)
    if int(position.qty) < 0:
        print(f'Short position open for {ticker}')