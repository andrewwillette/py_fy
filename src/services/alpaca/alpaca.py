import alpaca_trade_api as tradeapi

api = tradeapi.REST()
account = api.get_account()

class Alpaca:
    @staticmethod
    def buyMarketBracketOrder(ticker, take_limit, stop_limit, quantity):
        api.submit_order(
            symbol=ticker,
            side='buy',
            type='market',
            qty=quantity,
            time_in_force='day',
            order_class='bracket',
            take_profit=dict(
                limit_price=take_limit
            ),
            stop_loss=dict(
                stop_price=stop_limit
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
    def getTickerPrice(ticker):
        return "not implemented yet"

    @staticmethod
    def listPositions():
        return api.list_positions()