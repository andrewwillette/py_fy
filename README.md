% PY_FY(1) Version 1.0

NAME
====

**py_fy.py** — Generates textual and graphical financial data. 

SYNOPSIS
========

| **python py_fy.py** TICKER \[**-gp**|**--graphprice** _daterange_] \[**-gv**|**--graphvolume** _daterange_]

DESCRIPTION
===========

Generates useful information regarding stocks, logging both text and graphs as requested.

Options
-------

-h, --help

:   Prints brief usage information.

-gp, --graphprice DATE_RANGE

:   Generates a graph of TICKER prices in DATE_RANGE 

-gv, --graphvolume DATE_RANGE

:   Generates a graph of TICKER trading volumes in DATE_RANGE

-t, --trade

:   Tries to make some smart decisions in the Alpaca paper trading environment. Outputs its dealings to the logs file.

ENVIRONMENT VARIABLES
===========

** IEX_TOKEN **
: Required
: API Token for making calls to iex cloud services, the store of financial information.
See [here](https://iexcloud.io) for receiving access.

** PY_FY_DOWNLOAD_DIR **
:  Optional
:  Location to download generated graphs. If unspecifed, defaults to 'py_fy/dist' 

** APCA_API_BASE_URL ** 
:   Required for trading
:   See [here](https://app.alpaca.markets/paper) for info regarding alpaca API connections.
** APCA_API_KEY_ID ** 
:   Required for trading.
** APCA_API_SECRET_KEY ** 
:   Required for trading.

AUTHOR
======

Andrew Willette <willette.andrew1846@gmail.com>

