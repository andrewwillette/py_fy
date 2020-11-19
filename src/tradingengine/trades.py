import math

from services.alpaca.alpaca import Alpaca, api


class Trades:
    @staticmethod
    def bracketOrder(symbol, quantityDollars):
        askprice = Alpaca.getAskPrice(symbol)
        take_price = askprice * 1.02
        stop_price = askprice * .993
        quantity = math.floor(quantityDollars/askprice)
        Alpaca.buyMarketBracketOrder(symbol, take_price, stop_price, quantity)

    @staticmethod
    def shortOrder(symbol, quantityDollars):
        # Submit a market order to open a short position of one share
        order = api.submit_order(symbol, 1, 'sell', 'market', 'day')
        print("Market order submitted.")

        # Submit a limit order to attempt to grow our short position
        # First, get an up-to-date price for our symbol
        symbol_bars = api.get_barset(symbol, 'minute', 1).df.iloc[0]
        symbol_price = symbol_bars[symbol]['close']
        print('symbol price is ' + str(symbol_price))
        # Submit an order for one share at that price
        order = api.submit_order(symbol, 1, 'sell', 'limit', 'day', symbol_price)
        print("Limit order submitted.")

        # Wait a second for our orders to fill...
        print('Waiting...')
        time.sleep(1)

        # Check on our position
        position = api.get_position(symbol)
        if int(position.qty) < 0:
            print(f'Shorting the close position open for {symbol}')
