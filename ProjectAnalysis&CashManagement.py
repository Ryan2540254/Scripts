import numpy  as np
import pandas as pd

class NPVA:
    def _init_(self,years,cost,rate,cflow):
        self.years = years
        self.cost  = cost
        self.rate  = rate
        self.cflow = cflow        
    def npva(self):
        npva = (self.cflow*((1-pow((1+self.rate),(-self.years)))/self.rate))-self.cost
        pi   = (self.cflow*((1-pow((1+self.rate),(-self.years)))/self.rate))/self.cost
        PI   = round(pi,3)
        print('The NPV for the project is:',round(npva,2))
        print('The Profitabiity Index is:',PI)

class NPVNA:
    def _init_(self,years,cost,rate,cflow):
        self.years = years
        self.cost  = cost
        self.rate  = rate
        self.cflow = cflow
    def npvna(self):        
        n  = int(self.years)
        lst=[]
        for i in range(0,n):
            List = int(input('Enter the years(List):'))
            lst.append(List)
        lst2=[]
        for i in range(0,n):
            List2 = int(input('Enter the yearly Cflows(List):'))
            lst2.append(List2)
            
        df = pd.DataFrame({'Years':lst,
                          'CFlows':lst2})        
        DCF = df['CFlows']/(pow((1+self.rate),df['Years']))
        df['DCFs']=round(DCF,3)
        df['CumSum of DCFs']=df['DCFs'].cumsum()
        df['CumSum of DCFs minus Cost']=df['CumSum of DCFs']-self.cost
        print(df)
        SDCFs = df['DCFs'].sum()
        print('The Sum of the Discounted CashFlows is:',(round(SDCFs,3)))
        NpvNtAnn = SDCFs - int(self.cost)
        PIn= SDCFs/self.cost
        print('The NPV of the Project is:',round(NpvNtAnn,2))
        print('The Profitability Index of the project is:{}.'.format(round(PIn,3)))
        # if df['CumSum of DCFs']
        # How to find when someone breakseven??
class CManagement:
    def _init_(self,costpt,tcash,oppc):
        self.costpt = costpt
        self.tcash  = tcash
        self.oppc   = oppc 
    def BaumolModel(self):
        OptCash = np.sqrt(2*self.costpt*self.tcash/self.oppc)
        return 'The optimum Amount Of cash under the Baumol Model is:{}'.format(round(OptCash,2))
# class CManagemnt:
#     def _init(self,)
        

print('Current Features are Cash Management & Project Analysis')      
ans = input('Which Analysis is being undertaken:')   
      
if ans.lower().split() == ['cash', 'management']:
    cashm = CManagement()
    cashm.costpt = float(input('Enter the Cost Per Transaction:'))
    cashm.tcash  = float(input('Enter the Total Cash Needed for Transactions During the year:'))
    cashm.oppc   = float(input('Enter the Opportunity Cost of Holding Cash(Rate of Return on Marketable Securities):'))
    print(cashm.BaumolModel())  
elif ans.lower().split() == ['project', 'analysis']:
    print('Class Options are:Annuity & NtAnnuity')       
    prj2 = input('Enter the class of the Project:')
    if prj2.lower() == 'annuity':
        prj2= NPVA()
        prj2.years  =   int(input('Enter the no.of years:'))
        prj2.cost   =   int(input('Enter the cost of the project:'))
        prj2.rate   = float(input('Enter the rate:'))
        prj2.cflow  =   int(input('Enter the Annual CashFlow:'))
        prj2.npva()
    elif prj2.lower() == 'ntannuity':
        prj2 = NPVNA()
        prj2.years  =      (input('Enter the no.of years:'))
        prj2.cost   =   int(input('Enter the cost of the project:'))
        prj2.rate   = float(input('Enter the rate:'))    
        prj2.npvna()
    
     

    
   

        
        




