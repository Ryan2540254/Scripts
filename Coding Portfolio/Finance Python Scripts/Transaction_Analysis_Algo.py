#!/usr/bin/env python3
import csv
import decimal
from   datetime   import datetime
from   time       import sleep
from   decimal    import Decimal
from   statistics import mean, median

from decimal import Decimal, InvalidOperation

def get_entries_count():
    try:
        entries_count = int(input('Enter the number of entries you want to make: '))
        if entries_count <= 0:
            print('Please enter a valid positive number of entries.')
            return get_entries_count()
        return entries_count
    except ValueError:
        print('Invalid input. Please enter a valid number.')
        return get_entries_count()

def get_entry_date():
    try:
        date_str = input('Enter the date for the entry (YYYY-MM-DD): ')
        entry_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        return entry_date
    except ValueError:
        print('Invalid date format. Please enter the date in the format YYYY-MM-DD.')
        return get_entry_date()

def add_entry(entry_type, entries_count):
    entry_list = []
    fieldnames = ['Date', 'Expense', 'Expense Amount', 'Revenue', 'Revenue Amount']
    
    with open('Accounting.csv', 'a+', newline='') as f:  # Corrected filename
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
        if f.tell() == 0:
            csv_writer.writeheader()

        for _ in range(entries_count):
            entry_dict            = {}
            entry_dict['Date']    = get_entry_date()
            entry_name            = input(f'Enter the {entry_type} name:')
            entry_amount          = input(f'Enter the {entry_name} amount:')

            try:
                entry_amount = int(entry_amount)
                if entry_amount > 0:
                    entry_dict[entry_type] = entry_name
                    entry_dict[f'{entry_type} Amount'] = entry_amount
                    entry_list.append(entry_dict)
                    # Only include relevant fields for the entry type being added
                    csv_writer.writerow({'Date': entry_dict['Date'], f'{entry_type}': entry_name, f'{entry_type} Amount': entry_amount})
                else:
                    print(f'Amount entered for {entry_name} isn\'t valid.')
            except ValueError:
                print(f'Invalid input. Please enter a valid number for the {entry_type} amount.')

def acc_analysis():
    with open('Accounting.csv', 'r+') as f:  # Corrected filename
        reader = csv.DictReader(f)
        expenses = []
        revenues = []

        for row in reader:
            if row['Expense Amount']:
                expenses.append(int(row['Expense Amount']))
            if row['Revenue Amount']:
                revenues.append(int(row['Revenue Amount']))

        print('\nExpense Analysis:')
        if not expenses:
            print('No expenses recorded.')
        else:
            print(f'Sum of Expenses: {sum(expenses)}')
            print(f'Mean of Expenses: {mean(expenses)}')
            print(f'Median of Expenses: {median(expenses)}')

        print('\nRevenue Analysis:')
        if not revenues:
            print('No revenues recorded.')
        else:
            print(f'Sum of Revenues: {sum(revenues)}')
            print(f'Mean of Revenues: {mean(revenues)}')
            print(f'Median of Revenues: {median(revenues)}')

def transaction_analysis():
    try:
        print('Choose the type of analysis:')
        print('1. Expense Analysis')
        print('2. Revenue Analysis')

        choice = input('Enter your selection: ')

        with open('Accounting.csv', 'r') as f:  # Corrected filename
            reader = csv.DictReader(f)
            names = set()

            if choice == '1':
                print('Expense Names:')
                for row in reader:
                    if row['Expense']:
                        names.add(row['Expense'])
                print(', '.join(names))

                f.seek(0)  # Reset the file position to the beginning

                expense_name = input('Enter the Expense name for analysis: ')
                filtered_rows = [row for row in reader if row['Expense'] == expense_name]

                if filtered_rows:
                    expenses = [int(row['Expense Amount']) for row in filtered_rows if row['Expense Amount']]
                    print(f'\nAnalysis for {expense_name}:')
                    print(f'Sum of {expense_name}: {sum(expenses)}')
                    print(f'Mean of {expense_name}: {mean(expenses)}')
                    print(f'Median of {expense_name}: {median(expenses)}')
                else:
                    print(f'No entries found for {expense_name}.')

            elif choice == '2':
                print('Revenue Names:')
                for row in reader:
                    if row['Revenue']:
                        names.add(row['Revenue'])
                print(', '.join(names))

                f.seek(0)  # Reset the file position to the beginning

                revenue_name = input('Enter the Revenue name for analysis: ')
                filtered_rows = [row for row in reader if row['Revenue'] == revenue_name]

                if filtered_rows:
                    revenues = [int(row['Revenue Amount']) for row in filtered_rows if row['Revenue Amount']]
                    print(f'\nAnalysis for {revenue_name}:')
                    print(f'Sum of {revenue_name}: {sum(revenues)}')
                    print(f'Mean of {revenue_name}: {mean(revenues)}')
                    print(f'Median of {revenue_name}: {median(revenues)}')
                else:
                    print(f'No entries found for {revenue_name}.')

            else:
                print('Invalid Selection. Please enter 1 or 2.')

    except Exception as e:
        print('There is an error. \n'
              'Kindly review the script. \n'
              f'Error Message: {e}')

    try:
        with open('Accounting.csv', 'r') as f:
            reader = csv.DictReader(f)
            expenses_dict = {}
            revenues_dict = {}
            total_expenses = Decimal(0)
            total_revenues = Decimal(0)

            if not reader.fieldnames or 'Expense' not in reader.fieldnames or 'Expense Amount' not in reader.fieldnames \
                    or 'Revenue' not in reader.fieldnames or 'Revenue Amount' not in reader.fieldnames:
                print("CSV file does not contain the required columns.")
                return

            for row_num, row in enumerate(reader, start=1):
                try:
                    expense_amount = Decimal(row.get('Expense Amount', '0').strip())
                    revenue_amount = Decimal(row.get('Revenue Amount', '0').strip())

                    if expense_amount > Decimal(0):
                        expenses_dict[row['Expense']] = expenses_dict.get(row['Expense'], Decimal(0)) + expense_amount
                        total_expenses += expense_amount
                        total_expenses = float(total_expenses)

                    if revenue_amount > Decimal(0):
                        revenues_dict[row['Revenue']] = revenues_dict.get(row['Revenue'], Decimal(0)) + revenue_amount
                        total_revenues += revenue_amount
                        total_revenues = float(total_revenues)

                except decimal.ConversionSyntax as e:
                    print(f"Error converting data in row {row_num}: {e}")

            print('\nFull Analysis - Sum of Transactions for Each Transaction Name:')
            print('\nExpense Analysis:')
            for expense, amount in expenses_dict.items():
                print(f'Sum of {expense}: {amount}')

            print('\nRevenue Analysis:')
            for revenue, amount in revenues_dict.items():
                print(f'Sum of {revenue}: {amount}')

            print('\nFinancial Metrics:')
            print(f'Total Expenses: {total_expenses}')
            print(f'Total Revenues: {total_revenues}')

            net_income = total_revenues - total_expenses
            print(f'Net Income: {net_income}')

            if total_revenues != Decimal(0):
                gross_profit_margin = round(((total_revenues - total_expenses) / total_revenues * Decimal(100)), 2)
                print(f'Gross Profit Margin: {gross_profit_margin}%')
                

    except FileNotFoundError:
        print("File not found. Please ensure 'Accounting.csv' exists.")
    except Exception as e:
        print('An error occurred:')
        print(f'Error Message: {e}')


def full_analysis():
    try:
        with open('Accounting.csv', 'r') as f:
            reader = csv.DictReader(f)
            expenses_dict = {}
            revenues_dict = {}
            total_expenses = Decimal(0)
            total_revenues = Decimal(0)

            if not reader.fieldnames or 'Expense' not in reader.fieldnames or 'Expense Amount' not in reader.fieldnames \
                    or 'Revenue' not in reader.fieldnames or 'Revenue Amount' not in reader.fieldnames:
                print("CSV file does not contain the required columns.")
                return

            for row_num, row in enumerate(reader, start=1):
                try:
                    expense_amount_str = row.get('Expense Amount', '0').strip()
                    revenue_amount_str = row.get('Revenue Amount', '0').strip()

                    # Attempt to convert expense amount to Decimal
                    if expense_amount_str:
                        expense_amount = Decimal(expense_amount_str)
                        if expense_amount > Decimal(0):
                            expenses_dict[row['Expense']] = expenses_dict.get(row['Expense'], Decimal(0)) + expense_amount
                            total_expenses += expense_amount
                    else:
                        print(f"Error: Expense amount missing in row {row_num}")

                    # Attempt to convert revenue amount to Decimal
                    if revenue_amount_str:
                        revenue_amount = Decimal(revenue_amount_str)
                        if revenue_amount > Decimal(0):
                            revenues_dict[row['Revenue']] = revenues_dict.get(row['Revenue'], Decimal(0)) + revenue_amount
                            total_revenues += revenue_amount
                    else:
                        print(f"Error: Revenue amount missing in row {row_num}")
                        
                except InvalidOperation as e:
                    print(f"Error converting data in row {row_num}: {e}")

            print('\nFull Analysis - Sum of Transactions for Each Transaction Name:')
            print('\nExpense Analysis:')
            for expense, amount in expenses_dict.items():
                print(f'Sum of {expense}: {amount}')

            print('\nRevenue Analysis:')
            for revenue, amount in revenues_dict.items():
                print(f'Sum of {revenue}: {amount}')

            print('\nFinancial Metrics:')
            print(f'Total Expenses: {total_expenses}')
            print(f'Total Revenues: {total_revenues}')

            net_income = total_revenues - total_expenses
            print(f'Net Income: {net_income}')

            if total_revenues != Decimal(0):
                gross_profit_margin = round(((total_revenues - total_expenses) / total_revenues * Decimal(100)), 2)
                print(f'Gross Profit Margin: {gross_profit_margin}%')
            input("Press Enter to continue...")
            
    except FileNotFoundError:
        print("File not found. Please ensure 'Accounting.csv' exists.")
    except Exception as e:
        print('An error occurred:')
        print(f'Error Message: {e}')


def main():
    try:
        print('Welcome to the Accounting Program!\n'
              'This program allows you to manage your financial records by capturing expenses and revenues.\n')

        print('You can perform the following actions:')
        print('1. Enter data for expenses or revenues.')
        print('2. Perform analysis on expenses and revenues.')
        print('3. Perform transaction-level analysis.')
        print('4. Perform a full analysis of all transactions.\n')

        ans_enter_data = input('Do you want to enter data? (y/n): ')

        if ans_enter_data.lower() == 'y':
            entries_count = get_entries_count()
            ans1 = input('Choose the Accounting Option. \n'
             'Enter 1 for Expense Accounting. \n'
             'Enter 2 for Revenue Accounting \n'
             'Enter your selection:')

            if ans1 == '1':
               add_entry('Expense', entries_count)  # Pass 'Expense' as the first argument
            elif ans1 == '2':
                 add_entry('Revenue', entries_count)  # Pass 'Revenue' as the first argument
            else:
                 print('Enter a Valid Selection.')

            acc_analysis()

            ans2 = input('\nDo you want to perform transaction analysis? (y/n): ')
            while ans2.lower() == 'y':
                transaction_analysis()
                ans2 = input('\nDo you want to perform another transaction analysis? (y/n): ')

            ans3 = input('\nDo you want to perform a Full Analysis? (y/n): ')
            if ans3.lower() == 'y':
                full_analysis()

        elif ans_enter_data.lower() == 'n':
            ans_analysis = input('Do you want to perform transaction analysis? (y/n): ')
            while ans_analysis.lower() == 'y':
                transaction_analysis()
                ans_analysis = input('\nDo you want to perform another transaction analysis? (y/n): ')

            ans_full_analysis = input('\nDo you want to perform a Full Analysis? (y/n): ')
            if ans_full_analysis.lower() == 'y':
                full_analysis()
            elif ans_full_analysis.lower() == 'n':
                print('No data entered or analysis performed.')
            else:
                print('Invalid Selection. Please enter y or n.')

    except Exception as e:
        print('There is an error. \n'
              'Kindly review the script. \n'
              f'Error Message: {e}')

if __name__ == '__main__':
    main()








