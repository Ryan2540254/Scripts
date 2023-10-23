#!/usr/bin/env python3
import os
path   = input('Enter the path of the file:')


if os.path.exists(path):
    if os.path.isdir(path):
        folder = os.listdir(path)
        for file in folder:
             print(file)
       
    
else:
    print(f"{folder} isn't a valid drirectory")

