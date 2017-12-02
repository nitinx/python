# 28 Nov 2017 | Zomato API

import requests
import json
from nxauth import NXAuth

base_url = "https://developers.zomato.com/api/v2.1"


def get_user_key():
    return NXAuth().key_zomato()[0]['API_KEY']


def get_categories(headers):
    response = requests.get(base_url + '/categories', params='', headers=headers).json()

    #print(response)
    #print(response['categories'])
    for category in range(len(response['categories'])):
        print(str(response['categories'][category]['categories']['id'])
              + ' ' + response['categories'][category]['categories']['name'])
    return 0


def get_cities(headers, query):
    response = requests.get(base_url + '/cities?q=' + query + '&count=1', params='', headers=headers).json()

    #print(response)
    print(str(response['location_suggestions'][0]['country_id'])
          + ' ' + str(response['location_suggestions'][0]['country_name'])
          + ' ' + str(response['location_suggestions'][0]['id'])
          + ' ' + response['location_suggestions'][0]['name'])
    return str(response['location_suggestions'][0]['id'])


def get_collections(headers, city_id):
    response = requests.get(base_url + '/collections?city_id=' + city_id, params='', headers=headers).json()

    #print(response)
    for collection in range(len(response['collections'])):
        print(str(response['collections'][collection]['collection']['collection_id'])
              + ' ' + str(response['collections'][collection]['collection']['res_count'])
              + ' ' + response['collections'][collection]['collection']['title']
              + ' ' + response['collections'][collection]['collection']['description']
              + ' ' + response['collections'][collection]['collection']['url']
              + ' ' + response['collections'][collection]['collection']['share_url'])
    return 0


def get_cuisines(headers, city_id):
    response = requests.get(base_url + '/cuisines?city_id=' + city_id, params='', headers=headers).json()

    #print(response)
    for cuisine in range(len(response['cuisines'])):
        print(str(response['cuisines'][cuisine]['cuisine']['cuisine_id'])
              + ' ' + response['cuisines'][cuisine]['cuisine']['cuisine_name'])
    return 0


def get_establishments(headers, city_id):
    response = requests.get(base_url + '/establishments?city_id=' + city_id, params='', headers=headers).json()

    #print(response)
    for establishment in range(len(response['establishments'])):
        print(str(response['establishments'][establishment]['establishment']['id'])
              + ' ' + response['establishments'][establishment]['establishment']['name'])
    return 0


def main():
    headers = {'Accept': 'application/json', 'user-key': get_user_key()}
    city = 'Bangalore'

    #get_categories(headers)
    city_id = get_cities(headers, city)
    #get_collections(headers, city_id)
    #get_cuisines(headers, city_id)
    get_establishments(headers, city_id)


if __name__ == '__main__':
    main()
