# Import the yfinance. 
#If you get module not found error the run !pip install yfinance from terminal
#The following script makes use of the library yfinance developed independently by ranaroussi
#https://github.com/ranaroussi

import yfinance as yf
import matplotlib.pyplot as plt
import os

#The filepath were to save the date is set here
#File for the full date
#Recomended format for title of the file StockName_Frec_Year_Month_DayBegin_DayEnd_Duration
filepath = os.path.join('/here/goes/your/path/File_Name.dat')
#Recomended format for title of the file for only one of the columns of the data, ex. "Open" price data.
#Format for the file StockName_Frec_Year_Month_DayBegin_DayEnd_Duration
filepath_O = os.path.join('/here/goes/your/path/File_Name.dat')

#To obtain data you need the ticker NAME of the stock you are intrested in. 
#Go to yahoofinance and look for the stock, it has a name in parenthesis thats the name ticker.
#For more information about tickers you can consult here in the package docuemntation
#https://github.com/ranaroussi/yfinance/wiki/Tickers

#As an example. Here is how to download the price of Grupo Rotoplas stock price for the last five days with 1 minute frequency
scraped_data = yf.download('AGUA.MX',interval='1min',period='5d')
#Here is how to download the price for the mentioned stock price for the last seven days with 1 minute frequency
#instead of using the parameter period the dates are specified manually, yhaoo finance only allows to download 1 min frequency
#date up to 7 days within the last 30 days.
#scraped_data = yf.download('AGUA.MX','2023-06-16','2023-06-22',interval='1d')

#Here the complete data is stored to a csv file. 
scraped_data.to_csv(filepath,header='True')
#Here only the column containing the open price is stored.
scraped_data['Open'].to_csv(filepath_O,header='True')

#Note that as long as the script is excuted the download is performed only once. To prevent being blacklisted I recomend
#to download first and the reopen the downloaded data and do the desired analysis using another script or software. 

#To quickly visualize the downloaded data the folowing lines graph some of the columns of the complete set of data.
scraped_data['Open'].plot()
plt.show()

scraped_data['Close'].plot()
plt.show()

