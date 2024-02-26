# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 15:18:15 2023

@author: ryangacherubbusiness"outlook.com"
"""
from time import sleep
import datetime as dt
import numpy as np
import pandas as pd
import pandas_datareader as wb
import matplotlib.pyplot as plt

class StockF:
    def __init__(self, name, site, year1, yearn):
        self.name = name
        self.site = site
        self.year1 = year1
        self.yearn = yearn

    def Scrapping(self):
        df = wb.DataReader(self.name, self.site, self.year1, self.yearn)
        print(df.columns)
        print()
        print(df.describe())
        print()
        n1 = (self.yearn).year - (self.year1).year
        # Analysis
        print('Stock Index {} has been analyzed for {} years.'.format((self.name).upper(), n1))
        print('The last Stock Entry was {}.'.format(df.iloc[-1]))
        print('The First Stock Entry was {}.'.format(df.iloc[1]))
        # Graphing
        df.plot()
        plt.title('Line Graph of {} {}-{}.'.format(self.name, self.year1, self.yearn))
        plt.show()
        # Saving as csv
        df.to_csv('{} {}-{}.csv'.format(self.name, (self.year1).year, (self.yearn).year))

    def Cv(self):
        df = wb.DataReader(self.name, self.site, self.year1, self.yearn)
        CoVariation = (df[self.name].std() / df[self.name].mean()) * 100
        print('The Coefficient of Variation for {} is {} %.'.format(self.name, round(CoVariation, 2)))

    def Cv2(self):
        df = wb.DataReader(self.name, self.site, self.year1, self.yearn)
        CoVariation = (df[self.name].std() / df[self.name].mean()) * 100
        return round(CoVariation, 2)

while True:
    print('Web Scrapping from fred.')
    n = int(input('Enter the No. of Stocks to be Analysed:'))

    if n == 1:
        stk = StockF()
        stk.name = input('Enter the Stock Index: ')
        stk.site = input('Enter the Website From which data is retrieved: ')
        y1 = int(input('Enter the 1st Year: '))
        yn = int(input('Enter the nth Year: '))
        print()
        stk.year1 = dt.datetime(y1, 1, 1)
        stk.yearn = dt.datetime(yn, 12, 31)
        stk.Scrapping()
        stk.Cv()
        exit_nw = input('Would you like to exit (Yes/No): ')
        if exit_nw.lower() == 'yes':
            break
        print('Returning to the beginning...')
        sleep(2)

    elif n == 2:
        Stock1 = StockF()
        Stock2 = StockF()
        Stock1.name = input('Enter the 1st Stock Index:')
        Stock2.name = input('Enter the 2nd Stock Index:')
        Stock1.site = input('Enter the Site to be Searched:')
        Stock2.site = Stock1.site
        y1 = int(input('Enter the 1st Year: '))
        yn = int(input('Enter the nth Year: '))
        print()
        Stock1.year1 = dt.datetime(y1, 1, 1)
        Stock1.yearn = dt.datetime(yn, 12, 31)
        Stock2.year1 = dt.datetime(y1, 1, 1)
        Stock2.yearn = dt.datetime(yn, 12, 31)
        Stock1.Scrapping()
        Stock1.Cv()
        Stock2.Scrapping()
        Stock2.Cv()
        # Analysis
        if Stock1.Cv2() > Stock2.Cv2():
            print('{} is the riskier option.'.format(Stock1.name))
            print('{} is the best option.'.format(Stock2.name))
        else:
            print('{} is the riskier option.'.format(Stock2.name))
            print('{} is the best option.'.format(Stock1.name))

        exit_nw = input('Would you like to exit (Yes/No): ')
        if exit_nw.lower() == 'yes':
            break
        print('Returning to the beginning...')
        sleep(2)

    elif n == 3:
        Stock1 = StockF()
        Stock2 = StockF()
        Stock3 = StockF()
        Stock1.name = input('Enter the 1st Stock Index:')
        Stock2.name = input('Enter the 2nd Stock Index:')
        Stock3.name = input('Enter the 3rd Stock Index:')
        Stock1.site = input('Enter the Site to be Searched:')
        Stock2.site = Stock1.site
        Stock3.site = Stock1.site
        y1 = int(input('Enter the 1st Year: '))
        yn = int(input('Enter the nth Year: '))
        print()
        Stock1.year1 = dt.datetime(y1, 1, 1)
        Stock1.yearn = dt.datetime(yn, 12, 31)
        Stock2.year1 = dt.datetime(y1, 1, 1)
        Stock2.yearn = dt.datetime(yn, 12, 31)
        Stock3.year1 = dt.datetime(y1, 1, 1)
        Stock3.yearn = dt.datetime(yn, 12, 31)
        Stock1.Scrapping()
        Stock1.Cv()
        Stock2.Scrapping()
        Stock2.Cv()
        Stock3.Scrapping()
        Stock3.Cv()
        # Analysis
        if Stock1.Cv2() > Stock2.Cv2() and Stock1.Cv2() > Stock3.Cv2():
            print('{} is the riskiest option.'.format(Stock1.name))

        elif Stock2.Cv2() > Stock1.Cv2() and Stock2.Cv2() > Stock3.Cv2():
            print('{} is the riskiest option.'.format(Stock2.name))

        elif Stock3.Cv2() > Stock1.Cv2() and Stock3.Cv2() > Stock2.Cv2():
            print('{} is the riskiest option.'.format(Stock3.name))

        if Stock1.Cv2() < Stock2.Cv2() and Stock1.Cv2() < Stock3.Cv2():
            print('{} is the best option.'.format(Stock1.name))

        elif Stock2.Cv2() < Stock1.Cv2() and Stock2.Cv2() < Stock3.Cv2():
            print('{} is the best option.'.format(Stock2.name))

        elif Stock3.Cv2() < Stock1.Cv2() and Stock3.Cv2() < Stock2.Cv2():
            print('{} is the best option.'.format(Stock3.name))

        exit_nw = input('Would you like to exit (Yes/No): ')
        if exit_nw.lower() == 'yes':
            break
        print('Returning to the beginning...')
        sleep(2)
