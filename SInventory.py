# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Created on Mon Aug 21 18:54:28 2023
@author: ADMIN
"""
"""Script for managing and updating the items in a site.
   This script allows users to manage and update items in a site's inventory.
   Users can add new items with their quantities or 
      update existing items by  subtracting quantities from the inventory.
   The script provides a user-friendly interface for interacting with the inventory.
"""

import datetime
import json
import os

print("This is a product of Infinite Solutions")
print('Incase of any queries contact ryangacherubusiness@outlook.com' + '\n')

site_names = ['A','B','C']
site_inventories = {site_name: {} for site_name in site_names}

def update_add_site():
    print("Available Sites Currently ongoing:")
    for index, site_name in enumerate(site_names,1):
        print(f'{index}:{site_name}')
       
    site_choice = int(input("Enter the number corresponding to the site: "))
    
    selected_site = site_names[site_choice - 1]
    current_date  = datetime.datetime.now().strftime('%Y-%m-%d')
    
    print("Available Functions are adding & updating."+ '\n')
    print("Adding means  adding a new tool to site inventory")
    print("Updating means increasing or reducing the qty of an existing item." + '\n')
    
    ositem         = selected_site 
    site_inventory = site_inventories[selected_site]
    ans            = input('Would you like to add or update:')
    print(f"Managing inventory for {selected_site} on {current_date}")
    
    if ans.lower() == 'add':
        nitems  = int(input('Enter the no of items to be added:'))
    
        for i in range(nitems):
            oitem        = input("Enter the item to be stored:")
            if oitem not in site_inventory:
                site_inventory[oitem] = int(input(f'Enter the no of {oitem} to be added to site store:'))
                save_file = f'{selected_site}_inventory.json'
                with open(save_file, 'w') as file:
                    json.dump(site_inventory,file)
            else:
                 print(f"{oitem} is already stored in the dictionary.")    
        print(f'For the {ositem} site the inventory is:')        
        print(f'Total Site Inventory As at {current_date} : {site_inventory}')
            
    elif ans.lower() == 'update':
        ans2 = input('Would you like to add or subtract:')
        
        if ans2.lower() == 'subtract':
            n_updates = input('Enter the item to be updated:')
            if n_updates in site_inventory:
                x = int(input(f'Enter the no of {n_updates} being taken from the site'))
                site_inventory[n_updates] -= x
                
                print(f'{x} {n_updates}s taken from site')
                print(f'New Total Site Inventory {site_inventory}')
                load_filename = f"{selected_site}_inventory.json"
                if os.path.exists(load_filename):
                      with open(load_filename, 'r') as file:
                           dict1 = json.load(file)
                      print(f'Inventory loaded from {load_filename}')
                else:
                     print(f'No previous inventory data found for {selected_site}')
            else:
                print(f"{n_updates} is not stored in {selected_site} Inventory.")
                
        elif ans2.lower() == 'add':
            n_updates = input('Enter the item to be updated:')
            if n_updates in dict1:
                x = int(input(f'Enter the no of {n_updates} being added to the site'))
                dict1[n_updates] += x
                print(f'{x} {n_updates}s added to site')
                print(f'New Total Site Inventory {dict1}')
            else:
                print(f"{n_updates} is not stored in {selected_site} Inventory.")
        else:
            print("Invalid choice.")
       
update_add_site()        
        
       
               
        
        

        
