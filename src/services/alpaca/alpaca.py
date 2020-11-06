import alpaca_trade_api as tradeapi

api = tradeapi.REST()
account = api.get_account()

class Alpaca:

    """
    Make a bracket order on a given stock
    stock : the stock to make order on
    take_limit : what we want, the price to sell stock once it gets that high
    stop_loss : a safety net to get out of the trade if it goes too far south
    """
    @staticmethod
    def buyMarketBracketOrder(stock, take_limit, stop_loss, quantity):
        api.submit_order(
            symbol=stock,
            side='buy',
            type='market',
            qty=quantity,
            time_in_force='day',
            order_class='bracket',
            take_profit=dict(
                limit_price=take_limit
            ),
            stop_loss=dict(
                stop_price=stop_loss
            )
        )
        return True

    @staticmethod
    def buyMarketOrder(ticker):
        api.submit_order(
            symbol=ticker,
            qty=1,
            side='buy',
            type='market',
            time_in_force='gtc'
        )
        return True

    @staticmethod
    def sellMarketOrder(ticker):
        api.submit_order(
            symbol=ticker,
            qty=1,
            side='sell',
            type='market',
            time_in_force='gtc'
        )
        return True

    @staticmethod
    def getTickerPosition(ticker):
        return api.get_position(ticker)

    @staticmethod
    def getAskPrice(ticker):
        ask_price = api.get_last_quote(ticker)._raw.get('askprice')
        return ask_price

    @staticmethod
    def listPositions():
        return api.list_positions()
