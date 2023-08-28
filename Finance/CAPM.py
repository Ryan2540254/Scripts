# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 14:06:07 2023

@author: ADMIN
"""
import statistics as st
import numpy      as np
n=    int(input('Enter the No. of Securities in Portfolio:'))
# def EReturn(RF,Bt):
#     return (RF+RP*Bt)*100
def Sec(n):
    if n==1:
        ER  = float(input('Enter the Expected Return in the market:'))
        RF  = float(input('Enter the Risk Free Rate:'))
        Bt  = float(input('Enter the Beta for the Security:'))
        RP  = ER-RF
        ERS = (RF+RP*Bt)*100
        print('The Risk Premium is:',RP)
        print('The Expected Return on the Security is:',round(ERS,2),'Percent')
    elif n==2:
        ER   = float(input('Enter the Expected Return in the market:'))
        RF   = float(input('Enter the Risk Free Rate:'))
        
        P1   = float(input('Enter the proportion of the 1st Security:'))
        P2   = float(input('Enter the proportion of the 2nd Security:'))
        
        Bt1  = float(input('Enter the Beta for the 1st Security:'))
        Bt2  = float(input('Enter the Beta for the 2nd Security:'))
        
        RP  = ER-RF
        ERS1 = (RF+RP*Bt1)*100
        ERS2 = (RF+RP*Bt2)*100
        BP   = P1*Bt1 + P2*Bt2
        ERP  = P1*ERS1 + P2*ERS2 
        
        print('The Risk Premium is:',RP)
        print('The Expected Return on the 1st Security is:',round(ERS1,2),'Percent')
        print('The Expected Return on the 2nd Security is:',round(ERS2,2),'Percent')
        print('The Expected Return on the Portfolio is:',round(ERP,2),'Percent')
        print('The Beta for the Portfolio is:',BP)
        
print(Sec(n))


