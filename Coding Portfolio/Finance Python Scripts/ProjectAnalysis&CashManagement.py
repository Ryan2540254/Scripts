import numpy as np
import pandas as pd

class NPVA:
    def __init__(self, years, cost, rate, cflow):
        self.years = years
        self.cost = cost
        self.rate = rate
        self.cflow = cflow

    def npva(self):
        npva = (self.cflow * ((1 - pow((1 + self.rate), (-self.years))) / self.rate)) - self.cost
        pi = (self.cflow * ((1 - pow((1 + self.rate), (-self.years))) / self.rate)) / self.cost
        PI = round(pi, 3)
        print('The NPV for the project is:', round(npva, 2))
        print('The Profitability Index is:', PI)

class NPVNA:
    def __init__(self, years, cost, rate, cflow):
        self.years = years
        self.cost = cost
        self.rate = rate
        self.cflow = cflow

    def npvna(self):
        n = int(self.years)
        lst = []
        for i in range(0, n):
            List = int(input('Enter the years(List):'))
            lst.append(List)
        lst2 = []
        for i in range(0, n):
            List2 = int(input('Enter the yearly Cflows(List):'))
            lst2.append(List2)

        df = pd.DataFrame({'Years': lst,
                           'CFlows': lst2})
        DCF = df['CFlows'] / (pow((1 + self.rate), df['Years']))
        df['DCFs'] = round(DCF, 3)
        df['CumSum of DCFs'] = df['DCFs'].cumsum()
        df['CumSum of DCFs minus Cost'] = df['CumSum of DCFs'] - self.cost
        print(df)
        SDCFs = df['DCFs'].sum()
        print('The Sum of the Discounted CashFlows is:', (round(SDCFs, 3)))
        NpvNtAnn = SDCFs - int(self.cost)
        PIn = SDCFs / self.cost
        print('The NPV of the Project is:', round(NpvNtAnn, 2))
        print('The Profitability Index of the project is:{}.'.format(round(PIn, 3)))

class CManagement:
    def __init__(self, costpt, tcash, oppc):
        self.costpt = costpt
        self.tcash = tcash
        self.oppc = oppc

    def BaumolModel(self):
        OptCash = np.sqrt((2 * self.costpt * self.tcash) / self.oppc)
        return 'The optimum Amount Of cash under the Baumol Model is:{}'.format(round(OptCash, 2))

print('Current Features are Cash Management & Project Analysis')
ans = input('Which Analysis is being undertaken:')

if ans.lower() == 'cash management':
    cashm = CManagement(float(input('Enter the Cost Per Transaction:')),
                        float(input('Enter the Total Cash Needed for Transactions During the year:')),
                        float(input('Enter the Opportunity Cost of Holding Cash(Rate of Return on Marketable Securities):')))
    print(cashm.BaumolModel())
elif ans.lower() == 'project analysis':
    print('Class Options are:Annuity & NtAnnuity')
    prj2 = input('Enter the class of the Project:')
    if prj2.lower() == 'annuity':
       try:
            prj2 = NPVA(int(input('Enter the no.of years:')),
                    int(input('Enter the cost of the project:')),
                    float(input('Enter the rate:')),
                    int(input('Enter the Annual CashFlow:')))
            prj2.npva()
       except ValueError:
           print('Invalid input. Please enter numeric values for years, cost, rate, and cash flow.')

    elif prj2.lower() == 'ntannuity':
        try:
            prj2 = NPVNA(int(input('Enter the no.of years:')),
                     int(input('Enter the cost of the project:')),
                     float(input('Enter the rate:')))
            prj2.npvna()
        except ValueError:
            print('Invalid input. Please enter numeric values for years, cost, rate, and cash flow.')
    else:
        print('Invalid Selection. Please choose either "Annuity" or "NtAnnuity".')
        
