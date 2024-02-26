# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 15:18:15 2023
"""
from   time          import sleep
import datetime          as dt
import numpy             as np
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
        n1 = self.yearn - self.year1
        # Analysis
        print('Stock Index {} has been analyzed for {} years.'.format((self.name).upper(), n1))
        print('The last Stock Entry was {}.'.format(df.iloc[-1]))
        print('The First Stock Entry was {}.'.format(df.iloc[0]))  # Changed from [1] to [0]
        # Graphing
        df.plot()
        plt.title('Line Graph of {} {}-{}.'.format(self.name, self.year1.strftime('%Y'), self.yearn.strftime('%Y')))
        plt.show()
        # Saving as csv
        df.to_csv('{} {}-{}.csv'.format(self.name, self.year1.strftime('%Y'), self.yearn.strftime('%Y')))


    def Cv(self):
        df = wb.DataReader(self.name, self.site, self.year1, self.yearn)
        CoVariation = (df[self.name].std() / df[self.name].mean()) * 100
        print('The Coefficient of Variation for {} is {} %.'.format(self.name, round(CoVariation, 2)))

    def Cv2(self):
        df = wb.DataReader(self.name, self.site, self.year1, self.yearn)
        CoVariation = (df[self.name].std() / df[self.name].mean()) * 100
        return round(CoVariation, 2)

def get_valid_input(message, input_type=int):
    while True:
        try:
            user_input = input(message)
            if input_type == int:
                return int(user_input)
            elif input_type == str:
                return user_input
        except ValueError:
            print("Invalid input. Please enter a valid value.")

while True:
    print('Web Scraping from fred.')
    n = get_valid_input('Enter the No. of Stocks to be Analyzed:', input_type=int)

    if n == 1:
        stk = StockF(
            name=get_valid_input('Enter the Stock Index: ', input_type=str),
            site=get_valid_input('Enter the Website From which data is retrieved: ', input_type=str),
            year1=get_valid_input('Enter the 1st Year: ', input_type=int),
            yearn=get_valid_input('Enter the nth Year: ', input_type=int)
        )
        print()
        stk.year1 = dt.datetime(stk.year1, 1, 1)  # Fixed initialization of datetime
        stk.yearn = dt.datetime(stk.yearn, 12, 31)
        stk.Scrapping()
        stk.Cv()
        exit_nw = get_valid_input('Would you like to exit (Yes/No): ', input_type=str)
        if exit_nw.lower() == 'yes':
            break
        print('Returning to the beginning...')
        sleep(2)

    elif n == 2:
        Stock1 = StockF(
            name=get_valid_input('Enter the 1st Stock Index:', input_type=str),
            site=get_valid_input('Enter the Site to be Searched:', input_type=str),
            year1=get_valid_input('Enter the 1st Year: ', input_type=int),
            yearn=get_valid_input('Enter the nth Year: ', input_type=int)
        )
        Stock2 = StockF(
            name=get_valid_input('Enter the 2nd Stock Index:', input_type=str),
            site=Stock1.site,
            year1=get_valid_input('Enter the 1st Year: ', input_type=int),  # Added missing comma
            yearn=get_valid_input('Enter the nth Year: ', input_type=int)
        )

        print()
        Stock1.year1 = dt.datetime(Stock1.year1, 1, 1)
        Stock1.yearn = dt.datetime(Stock1.yearn, 12, 31)

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

        exit_nw = get_valid_input('Would you like to exit (Yes/No): ', input_type=str)
        if exit_nw.lower() == 'yes':
            break
        print('Returning to the beginning...')
        sleep(2)

    elif n == 3:
        Stock1 = StockF(
            name=get_valid_input('Enter the 1st Stock Index:', input_type=str),
            site=get_valid_input('Enter the Site to be Searched:', input_type=str),
            year1=get_valid_input('Enter the 1st Year: ', input_type=int),
            yearn=get_valid_input('Enter the nth Year: ', input_type=int)
        )
        Stock2 = StockF(
            name=get_valid_input('Enter the 2nd Stock Index:', input_type=str),
            site=Stock1.site,
            year1=get_valid_input('Enter the 1st Year: ', input_type=int),  # Added missing comma
            yearn=get_valid_input('Enter the nth Year: ', input_type=int)
        )
        Stock3 = StockF(
            name=get_valid_input('Enter the 3rd Stock Index:', input_type=str),
            site=Stock1.site,
            year1=get_valid_input('Enter the 1st Year: ', input_type=int),  # Added missing comma
            yearn=get_valid_input('Enter the nth Year: ', input_type=int)
        )

        print()
        Stock1.year1 = dt.datetime(Stock1.year1, 1, 1)
        Stock1.yearn = dt.datetime(Stock1.yearn, 12, 31)
        Stock2.year1 = dt.datetime(Stock2.year1, 1, 1)
        Stock2.yearn = dt.datetime(Stock2.yearn, 12, 31)
        Stock3.year1 = dt.datetime(Stock3.year1, 1, 1)
        Stock3.yearn = dt.datetime(Stock3.yearn, 12, 31)
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

        exit_nw = get_valid_input('Would you like to exit (Yes/No): ', input_type=str)
        if exit_nw.lower() == 'yes':
            break
        print('Returning to the beginning...')
        sleep(2)
