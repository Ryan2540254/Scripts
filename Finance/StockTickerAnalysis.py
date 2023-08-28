import datetime                    as dt
import numpy                       as np
import yfinance                    as yf
import pandas                      as pd
import pandas_datareader           as wb
from pandas_datareader import data as pdr
import matplotlib.pyplot           as plt
plt.style.use('seaborn')


print('Kindly Note all Dates are to be in the format yyy-mm-dd')
stck  = input('Enter the Stock Index:')
y1    = input('Enter the Start year:')
yn    = input('Enter year N:')
start = dt.datetime.strptime(y1, '%Y-%m-%d')
end   = dt.datetime.strptime(yn,'%Y-%m-%d')


stck1 = yf.Ticker(stck)
df    = stck1.history(start=start,end=end,rounding=(True))
df1   = stck1.history(start=start,end=end,actions=False,rounding= True)
List  = ['Close','Dividends']
FList = ['Close','Open','High','Low']
# Analysis
print(df.describe())
print('The Analysis on Prices.')
print(df[FList].describe())
print('The Analysis of the Closing Prices & Dividends.')
print(df[List].describe())
print()
print('The Initial 5 prices')
print(df1.head())
print('The Last 5 prices')
print(df1.tail())
print()

print('The Initial Closing Price was',df['Close'].iloc[0])
print('The Last Closing Price was',df['Close'].iloc[-1])
print()
print('Reccomendation')
print(stck1.get_recommendations_summary)


print(stck1.financials)
print()
print('The Major ShareHolders')
print(stck1.major_holders)
print()
print('The Institional ShareHolding')
print(stck1.institutional_holders)
print()
print('The Earnings Dates.')
print(stck1.earnings_dates)


df[FList].plot()
plt.show()
df[List].plot()
plt.title('Line Graph of Close Price & Dividends')
plt.show()
