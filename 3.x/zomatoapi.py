# 28 Nov 2017 | Zomato API

import requests
import json

user_key = '96de02583dbb02fae87e834846ee7ee5'
headers = {'user-key': user_key}

results = requests.get('https://developers.zomato.com/api/v2.1/categories', params='', headers=headers).json()

print(results)


