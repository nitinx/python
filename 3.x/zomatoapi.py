# 28 Nov 2017 | Zomato API

import requests
import json
from nxauth import NXAuth

user_key = NXAuth().key_zomato()[0]['API_KEY']

headers = {'Accept': 'application/json', 'user-key': user_key}
resp_cats = requests.get('https://developers.zomato.com/api/v2.1/categories', params='', headers=headers).json()

print(resp_cats)
print(resp_cats['categories'])
print(len(resp_cats['categories']))

'''
for cat in range(len(resp_cats[1]['categories'])):
    print('\t"' + cat[1]['id'] + '","'
          + cat[1]['categories']['categories'][cat]['id'] + '","'
          + cat[1]['categories']['categories'][cat]['name'] + '"')
'''
