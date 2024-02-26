#!/usr/bin/env python3
import os
import requests

path = "/data/feedback/"
keys = ["title", "name", "date", "feedback"]

folder = os.listdir(path)
for file in folder:
    keycount = 0
    fb = {}
    with open(path +file) as fil:
         for line in fil:
             value              = line.strip()
             if keycount < len(keys):
                      fb[keys[keycount]] = value
                      keycount          +=  1
    response = requests.post("http://34.171.24.000/feedback/", json=fb)
    if response.status_code == 201:
       print('Successful')
       print(f'The  staus code is:{response.status_code}') 
    else:
         print('Operation not working.')
         print(f'The status code:{response.status_code}')
         print(response.text[:150])
