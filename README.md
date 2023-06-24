# General info
This script is intended to give access to intraday stock data. Intraday stock data is rarely found online for free and having a reliable and fast way to gather it may be a way to obtain such data. The code downloads data from yahoo finance and makes use of the python library written by ranaroussi (https://github.com/ranaroussi).

The script is set to download the maximum amount of prices with a frequency of 1 minute. Yahoo finance API allows to download up to 7 days within the last 30 days of such data.

# Libraries used
This script makes use of the following libraries
* matplotlib.pyplot - To make a quick graph of the scraped data. This is useful to validate that we downladed the correct data.
* os - To save the downloaded date to a file. This allow to manipulate the date once downloaded.
* yfinance - To call the yahoofinance API. This library was developed independently by ranaroussi (https://github.com/ranaroussi)

# Setup
To run this code is necessary to have installed the matplotlib and yfinance libraries.
Using pip is a fast way to setup such libraries

* To install pip run in terminal
python -m pip install -U pip

* To install matplotlib run in terminal
python -m pip install -U matplotlib 

* To install yfinance run in terminal
python -m pip install yfinance 

* To run the script
1. Go to the location where the script is saved and open a terminal at such path.
2. Run
python Scarper_1min_data.py

# On how to use it
Although the script has comments above the important lines of code here you can find the link to the github library by ranaroussi
https://github.com/ranaroussi/yfinance/wiki/Tickers

The parameters of the function yfinance.download have some restrictions imposed by the yahoo finances API and are detailed in the link above.



