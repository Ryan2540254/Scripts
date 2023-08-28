# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 17:45:26 2023

@author: ADMIN
"""
import numpy             as np
import datetime          as dt
import pandas            as pd
import pandas_datareader as wb
import matplotlib.pyplot as plt

def Cv(columns):
    return round((columns.std()/columns.mean())*100,3)
class Stock:
    def _init_(self,sindx,site,wk):
        self.sindx = sindx
        self.site  = site
        self.wk    = wk
    def SScrap(self):
        end   =       dt.datetime.now()
        start = end - dt.timedelta(weeks=self.wk)
        df    = wb.DataReader(self.sindx,self.site,start,end)
        print(df.columns)
        print('The Co-efficient of Variation is:',Cv(df[self.sindx]))
        print(df.describe())
        print(df.head())
        print(df.tail())
        print(df.iloc[0])
        print(df.iloc[-1])
        df.plot()
        plt.show()
    
n      = int(input('Enter The No. of Stocks to be evaluated:'))
if n == 1:
    Stock1 = Stock()  
    Stock1.sindx =     input('Enter the Stock Index:')  
    Stock1.site  =     input('Enter the Site to be Searched:')
    Stock1.wk    = int(input('Enter the no. of weeks(From Current Time):'))        
    print(Stock1.SScrap())
elif n==2:
    Stock1 = Stock() 
    Stock2 = Stock()
    Stock1.sindx =     input('Enter the 1st Stock Index:') 
    Stock2.sindx =     input('Enter the 2nd Stock Index:') 
    Stock1.site  =     input('Enter the Site to be Searched:')
    Stock2.site  =     Stock1.site
    Stock1.wk    = int(input('Enter the no. of weeks(From Current Time):'))
    Stock2.wk    =     Stock1.wk        
    print(Stock1.SScrap())
    print(Stock2.SScrap())

elif n==3:
    Stock1 = Stock() 
    Stock2 = Stock()
    Stock3 = Stock()
    Stock1.sindx =     input('Enter the 1st Stock Index:') 
    Stock2.sindx =     input('Enter the 2nd Stock Index:')
    Stock3.sindx =     input('Enter the 3rd Stock Index:')
    Stock1.site  =     input('Enter the Site to be Searched:')
    Stock2.site  =     Stock1.site
    Stock3.site  =     Stock1.site
    Stock1.wk    = int(input('Enter the no. of weeks(From Current Time):'))
    Stock2.wk    =     Stock1.wk  
    Stock3.wk    =     Stock1.wk      
    print(Stock1.SScrap())
    print(Stock2.SScrap())
    print(Stock3.SScrap())





        
    

