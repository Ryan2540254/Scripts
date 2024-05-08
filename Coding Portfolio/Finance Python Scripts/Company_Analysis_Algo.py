#!/usr/bin/env python
import os
import statistics
import pandas            as pd 
from   statistics    import mean,median,stdev

## Following Rates are Dated 6th May 2024.
Inflation_Rate_2023       = 0.063
Yearly_TBill_Rate         = 0.164924

def Load_Doc():
    try:
        ##This Program is intended for analyzing CSV documents as such when inputting the name be 
        ##  sure to add '.csv' at the end e.g Book.csv
        doc        = input('Enter the name of the Document to be analyzed: ')
        path       = 'C:/Users/Ryan/ScriptWorkSpace/In Progess/Current Project/'
        fullpath   = os.path.join(path,doc)
        print(fullpath)
        df = pd.read_csv(fullpath)

        ## Analysis
        ans = input('Would you Like a Summarized Overview (Y/N): ')
        if ans.lower() == 'y': 
           print(df[['Expense Amount','Revenue Amount']].describe())

        
        print('This is an Overview of the company Expenses & Revenues \n')
        print('The Mean of the Expense and Revenue Amounts respectively: ')
        print(df[['Expense Amount','Revenue Amount']].mean() ,'\n')

        print('The Sum of the Expense and Revenue Amounts respectively: ')
        print(df[['Expense Amount','Revenue Amount']].sum() , '\n')

        profit = df['Revenue Amount'].sum() - df['Expense Amount'].sum() 
        profitmargin = (profit / df['Expense Amount'].sum() ) * 100
        roundedoff_profitmargin = round(profitmargin,2)
        print(f'The Current Profit of the Company is: {profit} \n')

        ans2     = input('Would you like the Analysis of the Company (Y/N): ')
        if ans2.lower() == 'y':
                if profit == 0 :
                    print('\n')
                    print('Company Analysis')
                    print('   - The Company is currently breaking even with Revenue being equal to Expense \n')
                    print('Recommended Actions : \n')
                    print('   - Look for additional Revenue Streams.')
                    print('   - Look for ways to reduce Company Expenses.')

                elif profit > 0:
                    print('\n')
                    print('Company Analysis')
                    print(f'  - The Company is currently making a profit : KES {profit}') 
                    print(f"  - The Company's Current Profit Margin is {roundedoff_profitmargin} %")
                    if Yearly_TBill_Rate*df['Expense Amount'].sum() > profit:
                        TBill_revenue = Yearly_TBill_Rate*df['Expense Amount'].sum()
                        TBill_revenue_roundedoff = round(TBill_revenue,2)
                        Diff_in_revenue = TBill_revenue_roundedoff - profit
                        Rounded_Diff = round(Diff_in_revenue,2)
                        print(f'If the Company invested in the 364 T-Bill revenue would be: KES {TBill_revenue_roundedoff} \n')
                        print('Recommended Actions : ')
                        print(f'  - The Company would have made greater profits investing in the Yearly T-Bill.')
                        print(f'    ( The Difference in TBill revenue and Current Profits: KES {Rounded_Diff} )')
                    
                    
                elif profit < 0:
                    print('\n')
                    print('Company Analysis')
                    print('    - The Company is currently operating at a Loss.')
                    print(f'   - Presently Company Profits are in the negative : KES {profit}  \n')
                    TBill_revenue = Yearly_TBill_Rate*df['Expense Amount'].sum()
                    TBill_revenue_roundedoff = round(TBill_revenue,2)
                    print(f'   - If the Company invested in the 364 T-Bill revenue would be: KES {TBill_revenue_roundedoff}')
                    print('Recommended Actions : ')
                    print('    - Look for additional Revenue Streams.')
                    print('    - Consider Investing in Yealy T-Bill.')
                    print('    - Look for ways to reduce Company Expenses.')
            
    except Exception as err:
        print(err)
        
def main():
            try:
               Load_Doc()
               input('Press Enter to exit.')
            except Exception as err:
                print(err)

if __name__ == '__main__':
    main()
