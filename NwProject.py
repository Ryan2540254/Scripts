# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 15:18:15 2023

@author: ryangacherubbusiness"outlook.com"
"""
from   time          import sleep
import datetime          as dt
import numpy             as np
import pandas            as pd
import pandas_datareader as wb
import matplotlib.pyplot as plt

class StockF:
    def _init_(self,name,site,year1,yearn):
        self.name  = name
        self.site  = site
        self.year1 = year1
        self.yearn = yearn
        
                
    def Scrapping(self):
        df = wb.DataReader(self.name,self.site,self.year1,self.yearn)
        print(df.columns)
        print()
        print(df.describe())
        print()
        n1 = (self.yearn).year - (self.year1).year
        # Analysis
        print('Stock Index {} has been analyzed for {} years.'.format((self.name).upper(),n1))
        print('The last Stock Price was {}.'.format(df.iloc[-1]))
        print('The First Stock Price was {}.'.format(df.iloc[0]))
        # Graphing
        df.plot()
        plt.title('Line Graph of {} {}-{}.'.format(self.name,self.year1,self.yearn))
        plt.show()
        # Saving as csv
        df.to_csv('{} {}-{}.csv'.format(self.name,(self.year1).year,(self.yearn).year))
        
    def Cv(self):
        df = wb.DataReader(self.name,self.site,self.year1,self.yearn)
        CoVariation = (df.std()/df.mean())*100
        print('The Coefficient of Variation for {} is {} %.'.format(self.name,round(CoVariation,2)))
        
while True:
 n        = int(input('Enter the No. of Stocks to be Analysed:'))
 stk      = StockF()
 stk.name = input('Enter the  Stock Index: ') 
 stk.site = input('Enter the Website From which data is retrieved: ')
 y1       = int(input('Enter the 1st Year: '))
 yn       = int(input('Enter the nth Year: '))
 print()
 stk.year1= dt.datetime(y1,1,1)
 stk.yearn = dt.datetime(yn,12,31)
 if n==1:
     stk.Scrapping()
     stk.Cv()
     exit_nw = input('Would you like to exit (Yes/No): ')
     if exit_nw.lower() == 'yes':
         break
     print('Returning to the beginning...')
     sleep(2)
        

        
        
