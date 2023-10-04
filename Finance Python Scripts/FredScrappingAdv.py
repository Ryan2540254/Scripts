import numpy             as np
import pandas            as pd
import pandas_datareader as wb
import matplotlib.pyplot as plt
import datetime          as dt
import array             as arr
import statistics        as st
from   functools     import lru_cache

while True:
    # Inputs
    n    = int(input('Enter the No. of Stocks to be Analysed:'))
    site =     input('Enter the Website From which data is retrieved: ')

    year1= int(input('Enter the 1st Year: '))
    yearn= int(input('Enter the nth Year: '))
    print()
    start= dt.datetime(year1,1,1)
    end  = dt.datetime(yearn,12,31)
    l    = yearn-year1
    
    # Functions
    def Cv(columns):
        return (columns.std()/columns.mean())*100
    @lru_cache()
    def stock(n):
        if n==1:
           start= dt.datetime(year1,1,1)
           end  = dt.datetime(yearn,12,31)
           a    =input('Enter the  Stock Index: ') 
           df1  = wb.DataReader(a,site,start,end)
           print('The Data Has been analyzed for',l,'years')
           print('The Coefficient of variation for the stock:',round(Cv(df1[a]),4))
           print(df1.columns)
           print(df1.describe())
           print('The Last Entry Price is:',df1.iloc[-1])
           print('The First Entry Price is:',df1.iloc[1])
           df1.plot()
           plt.title('Line Graph of {} from {} to {}.'.format(a,start,end))
           plt.legend()
           plt.show()
           df1.to_csv('{}from{}to{}.csv'.format(a,year1,yearn))           
        elif n==2:
           start= dt.datetime(year1,1,1)
           end  = dt.datetime(yearn,12,31)
           a    = input('Enter the 1st Stock Index: ')
           df1  = wb.DataReader(a,site,start,end)
           b    = input('Enter the 2nd Stock Index: ')
           df2  = wb.DataReader(b,site,start,end)
           # Cov  = np.cov(df1[a],df2[b])
           std1 = np.std(df1[a])      
           std2 = np.std(df2[b])
           
           print()
           
           # corr1 = Cov/(std1*std2)
           print('The Data Has been analyzed for',l,'years')
           print('The Coefficient of variation for the 1st:',round(Cv(df1[a]),4))
           print('The Coefficient of variation for the 2nd:',round(Cv(df2[b]),4))
           print('The Most Risky Stock has a Cv of:', max(round(Cv(df1[a]),4),
                                                          round(Cv(df2[b]),4)))
           print('The Least Risky Stock has a Cv of:',min(round(Cv(df1[a]),4),
                                                          round(Cv(df2[b]),4)))
           if Cv(df1[a])>Cv(df2[b]):
               print('The Best option after Risk Analysis is Stock:',b)
           elif Cv(df2[b])>Cv(df1[a]):
               print('The Best option after Risk Analysis is Stock:',a)
                
           print()      
           
           # print('The Coefficient of correlation:',corr1)
           # if df1[a].count() != df2[b].count():
           #     print('The Two Stocks dont have equal entries')
           # else:  print(np.corrcoef(df1[a],df2[b]))
           
           print(df1.columns)
           print(df1.describe())
           print('The Last Entry Price is:',df1.iloc[-1])
           print('The First Entry Price is:',df1.iloc[1])
           print()
           print(df2.columns)
           print(df2.describe())
           print('The Last Entry Price is:',df2.iloc[-1])
           print('The First Entry Price is:',df2.iloc[1])
           print()
           df1.plot()
           plt.legend()
           plt.show()
           df2.plot()
           plt.legend()
           plt.show()
        elif n==3:
           start= dt.datetime(year1,1,1)
           end  = dt.datetime(yearn,12,31)
           a    = input('Enter the 1st Stock Index: ')
           df1  = wb.DataReader(a,site,start,end)
           b    =input('Enter the 2nd Stock Index: ')
           df2  = wb.DataReader(b,site,start,end)
           c    =input('Enter the 3rd Stock Index: ')
           df3  = wb.DataReader(c,site,start,end)
           print('The Data Has been analyzed for',l,'years')
           print('The Coefficient of variation for the 1st:',round(Cv(df1[a]),4))
           print('The Coefficient of variation for the 2nd:',round(Cv(df2[b]),4))
           print('The Coefficient of variation for the 3rd:',round(Cv(df3[c]),4))
           print('The Most Risky Stock has a Cv of:',max(round(Cv(df1[a]),4),
                                                       round(Cv(df2[b]),4),
                                                       round(Cv(df3[c]),4)))
           print('The Least Risky Stock has a Cv of:',min(round(Cv(df1[a]),4),
                                                       round(Cv(df2[b]),4),
                                                       round(Cv(df3[c]),4)))
           if Cv(df1[a])<Cv(df2[b])and Cv(df1[a])<Cv(df3[c]):
               print('The Best option after Risk Analysis is Stock:',a)
           elif Cv(df2[b])<Cv(df1[a])and Cv(df2[b])<Cv(df1[c]):
               print('The Best option after Risk Analysis is Stock:',b)
           else: print('The Best option after Risk Analysis is Stock:',c)
           print()
           print(df1.columns)
           print(df1.describe())
           print('The Last Entry Price is:',df1.iloc[-1])
           print('The First Entry Price is:',df1.iloc[1])
           print()
           print(df2.columns)
           print(df2.describe())
           print('The Last Entry Price is:',df2.iloc[-1])
           print('The First Entry Price is:',df2.iloc[1])
           print()
           print(df3.columns)
           print(df3.describe())
           print('The Last Entry Price is:',df3.iloc[-1])
           print('The First Entry Price is:',df3.iloc[1])
           print()
           df1.plot()
           plt.legend()
           plt.show()
           df2.plot()
           plt.legend()
           plt.show()
           df3.plot()
           plt.legend()
           plt.show()
        elif n==4:
              start= dt.datetime(year1,1,1)
              end  = dt.datetime(yearn,12,31)
              a    = input('Enter the 1st Stock Index: ')
              df1  = wb.DataReader(a,site,start,end)
              b    =input('Enter the 2nd Stock Index: ')
              df2  = wb.DataReader(b,site,start,end)
              c    =input('Enter the 3rd Stock Index: ')
              df3  = wb.DataReader(c,site,start,end)
              d    =input('Enter the 4th Stock Index: ')
              df4  = wb.DataReader(d,site,start,end)
              print('The Data Has been analyzed for',l,'years')
              print('The Coefficient of variation for the 1st:',round(Cv(df1[a]),4))
              print('The Coefficient of variation for the 2nd:',round(Cv(df2[b]),4))
              print('The Coefficient of variation for the 3rd:',round(Cv(df3[c]),4))
              print('The Coefficient of variation for the 4th:',round(Cv(df4[d]),4))
              print('The Most Risky Stock has a Cv of:',max(round(Cv(df1[a]),4),
                                                          round(Cv(df2[b]),4),
                                                          round(Cv(df3[c]),4),
                                                          round(Cv(df4[d]),4)))
              print('The Least Risky Stock has a Cv of:',min(round(Cv(df1[a]),4),
                                                          round(Cv(df2[b]),4),
                                                          round(Cv(df3[c]),4),
                                                          round(Cv(df4[d]),4)))
              if Cv(df1[a])<Cv(df2[b])and Cv(df1[a])<Cv(df3[c]) and Cv(df1[a])<Cv(df4[d]) :
                  print('The Best option after Risk Analysis is Stock:',a)
              elif Cv(df2[b])<Cv(df1[a])and Cv(df2[b])<Cv(df3[c]) and Cv(df2[b])<Cv(df4[d]) :
                  print('The Best option after Risk Analysis is Stock:',b)
              elif Cv(df3[c])<Cv(df1[a])and Cv(df3[c])<Cv(df2[b]) and Cv(df3[c])<Cv(df4[d]):
                  print('The Best option after Risk Analysis is Stock:',c)
              else: print('The Best option after Risk Analysis is Stock:',d)
              print(df1.columns)
              print(df1.describe())
              print('The Last Entry Price is:',df1.iloc[-1])
              print('The First Entry Price is:',df1.iloc[1])
              print()
              print(df2.columns)
              print(df2.describe())
              print('The Last Entry Price is:',df2.iloc[-1])
              print('The First Entry Price is:',df2.iloc[1])
              print()
              print(df3.columns)
              print(df3.describe())
              print('The Last Entry Price is:',df3.iloc[-1])
              print('The First Entry Price is:',df3.iloc[1])
              print()
              print(df4.columns)
              print(df4.describe())
              print('The Last Entry Price is:',df4.iloc[-1])
              print('The First Entry Price is:',df4.iloc[1])
              print()
              df1.plot()
              plt.legend()
              plt.show()
              df2.plot()
              plt.legend()
              plt.show()
              df3.plot()
              plt.legend()
              plt.show()
              df4.plot()
              plt.legend()
              plt.show()
        elif n==5:
              start= dt.datetime(year1,1,1)
              end  = dt.datetime(yearn,12,31)
              a    = input('Enter the 1st Stock Index: ')
              df1  = wb.DataReader(a,site,start,end)
              b    =input('Enter the 2nd Stock Index: ')
              df2  = wb.DataReader(b,site,start,end)
              c    =input('Enter the 3rd Stock Index: ')
              df3  = wb.DataReader(c,site,start,end)
              d    =input('Enter the 4th Stock Index: ')
              df4  = wb.DataReader(d,site,start,end)
              e    =input('Enter the 5th Stock Index: ')
              df5  = wb.DataReader(e,site,start,end)
              print('The Data Has been analyzed for',l,'years')
              print('The Coefficient of variation for the 1st:',round(Cv(df1[a]),4))
              print('The Coefficient of variation for the 2nd:',round(Cv(df2[b]),4))
              print('The Coefficient of variation for the 3rd:',round(Cv(df3[c]),4))
              print('The Coefficient of variation for the 4th:',round(Cv(df4[d]),4))
              print('The Coefficient of variation for the 5th:',round(Cv(df5[e]),4))
              print('The Most Risky Stock has a Cv of:',max(round(Cv(df1[a]),4),
                                                          round(Cv(df2[b]),4),
                                                          round(Cv(df3[c]),4),
                                                          round(Cv(df4[d]),4),
                                                          round(Cv(df5[e]),4)))
              print('The Least Risky Stock has a Cv of:',min(round(Cv(df1[a]),4),
                                                          round(Cv(df2[b]),4),
                                                          round(Cv(df3[c]),4),
                                                          round(Cv(df4[d]),4),
                                                          round(Cv(df5[e]),4)))
              if Cv(df1[a])<Cv(df2[b])and Cv(df1[a])<Cv(df3[c]) and Cv(df1[a])<Cv(df4[d]) and Cv(df1[a])<Cv(df5[e]):
                  print('The Best option after Risk Analysis is Stock:',a)
              elif Cv(df2[b])<Cv(df1[a])and Cv(df2[b])<Cv(df3[c]) and Cv(df2[b])<Cv(df4[d]) and Cv(df2[b])<Cv(df5[e]) :
                  print('The Best option after Risk Analysis is Stock:',b)
              elif Cv(df3[c])<Cv(df1[a])and Cv(df3[c])<Cv(df2[b]) and Cv(df3[c])<Cv(df4[d]) and Cv(df3[c])<Cv(df5[e]) :
                  print('The Best option after Risk Analysis is Stock:',c)
              elif Cv(df4[d])<Cv(df1[a])and Cv(df4[d])<Cv(df2[b]) and Cv(df4[d])<Cv(df4[d]) and Cv(df4[d])<Cv(df5[e]) :
                  print('The Best option after Risk Analysis is Stock:',d)
              else:
                  print('The Best option after Risk Analysis is Stock:',e)
              print(df1.columns)
              print(df1.describe())
              print('The Last Entry Price is:',df1.iloc[-1])
              print('The First Entry Price is:',df1.iloc[1])
              print()
              print(df2.columns)
              print(df2.describe())
              print('The Last Entry Price is:',df2.iloc[-1])
              print('The First Entry Price is:',df2.iloc[1])
              print()
              print(df3.columns)
              print(df3.describe())
              print('The Last Entry Price is:',df3.iloc[-1])
              print('The First Entry Price is:',df3.iloc[1])
              print()
              print(df4.columns)
              print(df4.describe())
              print('The Last Entry Price is:',df4.iloc[-1])
              print('The First Entry Price is:',df4.iloc[1])
              print()
              print(df5.columns)
              print(df5.describe())
              print('The Last Entry Price is:',df5.iloc[-1])
              print('The First Entry Price is:',df5.iloc[1])
              print()
              df1.plot()
              plt.legend()
              plt.show()
              df2.plot()
              plt.legend()
              plt.show()
              df3.plot()
              plt.legend()
              plt.show()
              df4.plot()
              plt.legend()
              plt.show()
              df5.plot()
              plt.legend()
              plt.show()
    print(stock(n))  




        






