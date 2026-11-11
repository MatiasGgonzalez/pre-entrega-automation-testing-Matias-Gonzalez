import csv
import json

def read_users_csv():
    with open('data/users.csv', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)



def reader_productos_json():
    with open('data/products.json') as file:
        data = json.load(file)
        return data




"""
[

    {
        'usuario': 'standard_user', 
        'password': 'secret_sauce'
    },
    {
        'usuario': 'admin', 
        'password': '1234'
    },
    {
        'usuario': 'jose', 
        'password': '123'
    }
]
"""
