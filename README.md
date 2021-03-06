### PY_FY Version 0.1

src/py_fy.py — Generates textual and graphical financial data. Capable of actively trading on the alpaca platform with custom-configured rules. 

## SYNOPSIS

    python py_fy.py TICKER [ -s | --symbol SYMBOL] [ -gp | --graphprice DATE_RANGE ] [ -gv | --graphvolume DATE_RANGE ] [ -t | --trade ] [ -fv | --findvalue ]

## DESCRIPTION

Provided just the TICKER, will output various information regarding the security. 

-gp, --graphprice DATE_RANGE

- Generates a graph of TICKER prices in DATE_RANGE 
    
-gv, --graphvolume DATE_RANGE

- Generates a graph of TICKER trading volumes in DATE_RANGE

-t, --trade

- Tries to make smart decisions in the Alpaca paper trading environment. Outputs its dealings to the logs file.

-fv, --findvalue

- Tries to find stocks of value. Logs stocks of interest and reasons for interest.

-h, --help

- Prints brief usage information.

## ENVIRONMENT VARIABLES

Variable | Required | Description
------------ | ------------- | -------------
IEX_TOKEN | Yes | API Token for making calls to iex cloud services, the store of financial information. See [here](https://iexcloud.io) for receiving access. 
APCA_API_BASE_URL | If running with `--trade` argument | See [here](https://app.alpaca.markets/paper) for info regarding alpaca API connections.
APCA_API_KEY_ID | If running with `--trade` argument | See [here](https://app.alpaca.markets/paper) for info regarding alpaca API connections.
APCA_API_SECRET_KEY | If running with `--trade` argument | See [here](https://app.alpaca.markets/paper) for info regarding alpaca API connections. 
PYFY_GRAPH_DIR | No | Location to download generated graphs. Defaults to `py_fy/dist/graphs`

## AUTHOR

Andrew Willette <willette.andrew1846@gmail.com>

