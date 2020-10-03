Capabilities

Provides user access to historical and realtime stock information
  Iex Python API delivers real time and historical stock data. [PyPi reference](https://pypi.org/project/iexfinance/)
  Local postgreSql server which can save this data for more complex tasks.

Provides user with 
  Current available tables are
    historical_intraday
    balance_sheet

Provides user with real-time news releases
  newsapi python solution. [reference](https://newsapi.org/docs/client-libraries/python)

Provides user with some general data visualization queries
    Per stock:
        Show quote price by minute per day
          Done
        Show quote price by month for year
          Done
        Show volume over day
          Done

Instructions to Run Queries :

Get most recent price of TICKER : 
    TICKER --current

Generate graphs in dist/ folder 

Get daily graph of TICKER :
    TICKER --graph-daily
Get monthly graph of TICKER :
    TICKER --graph-monthly
Get yearly graph of TICKER :
    TICKER --graph-yearly

