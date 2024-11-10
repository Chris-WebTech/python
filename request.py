# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 14:39:14 2024

@author: Owner

--  Authors Note: [11/2024]
    In this example I was foring with a json file from
    a live store menu.
    Each menu item had a Unique 24 digit Identification
    Code.
    - The function Loops through all active products in 
      the url link display the Item name, product type, 
      and product price which is universal.
    - 'for c in x' creates another list to loop the ID 
      number and Display the last 4 digits.
    - Printing output to console
"""
# Import request library
# Sends a request to read the url Variable
import requests

# where to send the request
url = 'https://your/webpage/location.example'

# Store the Data from url
response = requests.get(url)

# Convert the data to json
json_data = response.json()

def brandGP():
    
    # Loop each Item, type, price as x in json_data
    for x in json_data:

        # store x as items output
        items = x['item'] + '\n' + x['type'] + '\n' + x['price'] + '\n'
        
        # loop last 4 - store in empty list elist
        for c in x:
            eList = []

            # store item id as list
            eList = x['id']
                
            # last for of each 24 digit id
            l4 = eList[20] + eList[21] + eList[22] + eList[23]

            # backfill with 0 if needed
            l4 = l4.zfill(4)

        print(l4 + '\n' + items)
def main():
    
    brandGP()

main()