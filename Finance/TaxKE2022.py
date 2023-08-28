# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 09:38:00 2023

@author: ADMIN
"""

import numpy             as np
import pandas            as pd
import matplotlib.pyplot as plt
import array             as arr
import statistics        as st

GTI = float(input('Enter the Gross Yearly Taxable Income:'))
MR  =   int(input('Enter the Yearly Mortgage Amount:'))
IRF =   int(input('Enter the Yearly Life Insuarance Amount:'))
ERF =   int(input('Enter the Yearly Education Relief Amount:'))
NSSF=   int(input('Enter the Yearly NSSF Contribution'))
OPAYE=  int(input('Enter the Yearly Overpaid PAYE:'))
print()
def NSSFF(GTI,NSSF):
        return min(((6/100)*GTI),25920,NSSF)
NTI= GTI-MR-NSSFF(GTI,NSSF)
def Tax(NTI):
    if   NTI<=288000:
        return (10/100)*NTI
    elif NTI>288000 and NTI<=388000:
        return (10/100)*288000+(25/100)*(NTI-288000)
    else:
        return 28800+25000+(30/100)*(NTI-388000)
def Mortgage(MR):
    return min(300000,MR)
def IRelief(IRF):
    IR= (15/100)*IRF
    return min(IR,60000)
def EdRelief(ERF):
    ER= (15/100)*ERF
    return min(ER,60000)
def TRelief(IRelief,EdRelief):
    return 28800+IRelief(IRF)+EdRelief(ERF)
PAYE=Tax(NTI)
TD  =Tax(NTI)-TRelief(IRelief)-OPAYE
OFF =TRelief(IRelief)+OPAYE

print('The Yearly Taxable Income less Mortgage Relief:',NTI)
print('The Monthly Taxable Income less Mortgage Relief:',round((NTI/12),2))
print('The Yearly PAYE  before Reliefs:',PAYE)
print('The Monthly PAYE  before Reliefs:',round((PAYE/12),2))
print()
print('The Total Yearly NSSF Deductions:',NSSFF(GTI,NSSF))
print('The Total Monthly NSSF Deductions:',round((NSSFF(GTI,NSSF)/12),2))
print('The Total Yearly Reliefs(Exc Mortgage)is:',TRelief(IRelief))
print('The Total Yearly Offsets Against Tax Liability(Inc PAYE)',OFF)
print()
print('The Yearly Tax Due After Reliefs:',TD)
print('The Monthly Tax Due After Reliefs:',round((TD/12),2))
print()
print('Monthly Salary before Tax:',round((NTI/12),2))
print('Monthly Salary after Tax: ',round(((GTI/12)-(TD/12)),2))
MSAT=(NTI/12)-round((TD/12),2)







