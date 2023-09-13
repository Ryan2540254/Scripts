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
print('Incase of any queries contact Provider' + '\n')

site_names = ['Site A','Site B','Site C','Site D']
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
    
    ans            = input('Would you like to add or update:')
    print(f"Managing inventory for {selected_site} on {current_date}")
    
    def Ans():
        site_inventory = site_inventories[selected_site]
        if ans.lower() == 'add':
            nitems  = int(input('Enter the no of items to be added:'))
            load_filename = f"{selected_site}_inventory.json"
            if os.path.exists(load_filename):
                with open(load_filename, 'r') as file:
                    site_inventory.update(json.load(file))
                print(f'Inventory loaded from {load_filename}')
            
            for i in range(nitems):
                oitem        = input("Enter the item to be stored:")
                if oitem not in site_inventory:
                    site_inventory[oitem] = int(input(f'Enter the no of {oitem} to be added to site store:'))
                    
                else:
                     print(f"{oitem} is already stored in the dictionary.")
                     
            # Save the updated inventory to file
            with open(load_filename, 'w') as file:
                json.dump(site_inventory, file)
            print('The Tool Addition was Successful.')
            print(f'For the {ositem} site the inventory is:')
            print(f'Total Site Inventory As at {current_date} : {site_inventory}')
                
        elif ans.lower() == 'update':
            ans2 = input('Would you like to add or subtract:')
            
            if ans2.lower() == 'subtract':
                load_filename = f"{selected_site}_inventory.json"
                if os.path.exists(load_filename):
                    with open(load_filename, 'r') as file:
                        site_inventory.update(json.load(file))
                        print(site_inventory)
                        print(f'Inventory loaded Successfully from: {load_filename}')
                        n_updates  = input('Enter the item in store to be updated: ')
                        if n_updates in site_inventory:
                            x     = int(input(f'Enter the no of {n_updates} to be removed from site store:'))
                            site_inventory[n_updates] -= x
                            print(f'{x} {n_updates} added to site.')
                            print(f'New Total Inventory for {selected_site} Site:{site_inventory}.')
                        else:

                            print(f"{n_updates} is not stored in {selected_site} Inventory.")

                else:
                        print('File does not exist.')
                        y = os.path.exists(load_filename)
                        print(f'Result of os.path.exists: {y}')
                with open(load_filename, 'w') as file:
                    json.dump(site_inventory, file)
                print('The Tool Update Subtraction was Successful.')
                print(f'For the {ositem} site the inventory is:')
                print(f'Total Site Inventory As at {current_date} : {site_inventory}')
              
            
        
            elif ans2.lower() == 'add':
                load_filename = f"{selected_site}_inventory.json"
                if os.path.exists(load_filename):
                    with open(load_filename, 'r') as file:
                        site_inventory.update(json.load(file))
                       
                        print(f'Inventory loaded Successfully from: {load_filename}')
                        print(site_inventory)
                        n_updates  = input('Enter the item in store to be updated: ')
                        if n_updates in site_inventory:
                            x     = int(input(f'Enter the no of {n_updates} to be added to site store:'))
                            site_inventory[n_updates] += x
                            print(f'{x} {n_updates} added to site.')
                            print(f'New Total Inventory for {selected_site} Site:{site_inventory}.')
                        else:
                            print(f"{n_updates} is not stored in {selected_site} Inventory.")
                
                else:
                        print('File does not exist.')
                        y = os.path.exists(load_filename)
                        print(f'Result of os.path.exists: {y}')
                
                # Save the updated inventory to file
                with open(load_filename, 'w') as file:
                    json.dump(site_inventory, file)
                print('The Tool Upate Addition was Successful.')
                print(f'For the {ositem} site the inventory is:')
                print(f'Total Site Inventory As at {current_date} : {site_inventory}')
                
               
                            
                        
                
            else:
                print("Invalid choice.")
                
    Ans()
       
update_add_site()        
        
       
               
        
        

        
