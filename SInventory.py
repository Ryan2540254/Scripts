# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Created on Mon Aug 21 18:54:28 2023
@author: ADMIN
"""
"""Script for managing and updating the items in a site.
   This script allows users to manage and update items in a site's inventory.
   Users can add new items with their quantities or 
      update existing items by  subtracting quantities from the inventory.
   The script provides a user-friendly interface for interacting with the inventory.
"""

print("This is a product of Infinite Solutions")
print('Incase of any queries contact ryangacherubusiness@outlook.com')
dict1 = {}
def update_add_site():
    ositem  = input("Enter the site name: ")
    ans     = input('Would you like to add or update:')
    if ans.lower() == 'add':
        nitems  = int(input('Enter the no of items to be added:'))

        for i in range(nitems):
            oitem        = input("Enter the items to be stored:")
            if i not in dict1:
                dict1[oitem] = int(input(f'Enter the no of {oitem} to be added to site store:'))
            else:
                 print(f"{oitem} is already stored in the dictionary.")    
        print(f'For the {ositem} the inventory is:')        
        print(f'Total Site Inventory{dict1}')
            
    elif ans.lower() == 'update':
        ans2 = input('Would you like to add or subtract:')
        
        if ans2.lower() == 'subtract':
            n_updates = input('Enter the item to be updated:')
            if n_updates in dict1:
                x = int(input(f'Enter the no of {n_updates} being taken from the site'))
                dict1[n_updates] -= x
                print(f'{x} {n_updates}s taken from site')
                print(f'New Total Site Inventory {dict1}')
            else:
                print(f"{n_updates} is not stored in the dictionary.")
                
        elif ans2.lower() == 'add':
            n_updates = input('Enter the item to be updated:')
            if n_updates in dict1:
                x = int(input(f'Enter the no of {n_updates} being added to the site'))
                dict1[n_updates] += x
                print(f'{x} {n_updates}s added to site')
                print(f'New Total Site Inventory {dict1}')
            else:
                print(f"{n_updates} is not stored in the dictionary.")
        else:
            print("Invalid choice.")
       
update_add_site()        
        
       
               
        
        

        
