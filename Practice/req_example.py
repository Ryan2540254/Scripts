#!/usr/bin/env python3

import requests
url      = input('Enter the url:')
response = requests.get(url)
if response.ok:
   """Will print True if response was good & False if not."""
   print(response.text[:150])
   response.raise_for_status()
