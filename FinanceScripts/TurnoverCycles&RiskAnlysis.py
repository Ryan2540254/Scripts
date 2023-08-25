from time import sleep

class Company:
    def _init_(self, ans, name, COGS, Sales, VCost, FCost, Intrst, OInventory, CInventory, OAccR, CAccR, OAccP, CAccP):
        self.name = name
        self.COGS = COGS
        self.Sales = Sales
        self.VCost = VCost
        self.FCost = FCost
        self.Intrst = Intrst
        self.OInventory = OInventory
        self.CInventory = CInventory
        self.OAccR = OAccR
        self.CAccR = CAccR
        self.OAccP = OAccP
        self.CAccP = CAccP
        self.ans = ans

    def Leverage(self):
        CMargin = self.Sales - self.VCost
        EBIT = CMargin - self.FCost
        EBT = EBIT - self.Intrst
        DOL = CMargin / EBIT
        DFL = EBIT / EBT
        DTL = DOL * DFL
        
        print()
        print('Risk Analysis for the Company:')
        print('The Degree of Operating Leverage is:', round(DOL, 3))
        print('The degree of Financial Leverage:', round(DFL, 3))
        print('The Degree of Total Leverage is:', round(DTL, 3))
        print('Risk Analysis based on Leverage:')
        print('If the sales increase by 1%, the Earnings Per Share will increase by {} % and vice versa.'.format(round(DTL, 3)))
        
        
    def Analysis(self):
        AI = (self.OInventory + self.CInventory) / 2
        AAR = (self.OAccR + self.CAccR) / 2
        AAP = (self.OAccP + self.CAccP) / 2

        IR = self.COGS / AI
        ARR = self.Sales / AAR
        APR = self.COGS / AAP

        IC = 365 / IR
        ARC = 365 / ARR
        APC = 365 / APR

        OC = IC + ARC
        ccc = OC - APC
        CCC = round(ccc, 3)
        print()
        print('The Working Capital Management Analysis For the Business:')
        print('The Inventory Turnover is:', IR, 'times')
        print('The Accounts Receivable Turnover is:', ARR, 'times')
        print('The Accounts Payable Turnover is:', APR, 'times')

        print('The Inventory Cycle is:', IC, 'days')
        print('The Daily Sales Outstanding is:', ARC, 'days')
        print('The Daily Payments Outstanding is:', APC, 'days')

        print('The Operating Cycle is:', OC, 'days')
        print('The Cash Conversion Cycle is:', CCC, 'days')

    def Discount(self):
        if self.ans:
            drate = float(input('Enter discount rate: '))
            ddate = int(input('Discount applies if full amount paid within: '))
            fdate = int(input('Client pays full amount after how many days (Limit): '))
            cdisc = (drate / (1 - drate)) * 365 / (fdate - ddate)
            CDisc = round(cdisc, 4)
            print('The Annual Cost of Discount is:', CDisc * 100, 'percent.')


while True:
    print('Cycles Analysis or Leverage Analysis')
    IAns = input('Enter the Analysis Being Carried out:')

    if IAns.lower().split() == 'Cycles Analysis'.lower().split():
        prj = Company()
        prj.COGS = int(input('Enter the C.O.G.S: '))
        prj.Sales = int(input('Enter the Credit Sales: '))
        prj.OInventory = int(input('Enter the Opening Inventory: '))
        prj.CInventory = int(input('Enter the Closing Inventory: '))
        prj.OAccR = int(input('Enter the Opening Accounts Receivable: '))
        prj.CAccR = int(input('Enter the Closing Accounts Receivable: '))
        prj.OAccP = int(input('Enter the Opening Accounts Payable: '))
        prj.CAccP = int(input('Enter the Closing Accounts Payable: '))
        prj.ans = bool(input('Is a discount offered? '))
        print('The Analysis for the client is:')
        prj.Analysis()
        prj.Discount()
        exit_nw = input('Would you like to exit (Yes/No): ')
        if exit_nw.lower() == 'yes':
            break
        print('Returning to the beginning...')
        sleep(2)

    elif IAns.lower().split() == 'leverage analysis'.lower().split():
        prj = Company()
        prj.Sales = int(input('Enter the Sales: '))
        prj.VCost = int(input('Enter the Variable Cost: '))
        prj.FCost = int(input('Enter the Fixed Cost: '))
        prj.Intrst = int(input('Enter the Interest Cost: '))
        prj.Leverage()
        exit_nw = input('Would you like to exit (Yes/No): ')
        if exit_nw.lower() == 'yes':
            break
        print('Returning to the beginning...')
        sleep(2)

    

print('Exiting the program...')
