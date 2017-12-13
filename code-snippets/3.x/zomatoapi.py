# 28 Nov 2017 | Zomato API

import requests
import json
from nxcommon import NXKey
from nxcommon import NXOracle

base_url = "https://developers.zomato.com/api/v2.1"
db_conn = NXOracle().db_login()
db_cur = db_conn.cursor()


def get_user_key():
    return NXKey().key_zomato()[0]['API_KEY']


def get_categories(headers):
    response = requests.get(base_url + '/categories', params='', headers=headers).json()

    db_cur.execute("truncate table ZMT_CATEGORIES")

    for category in range(len(response['categories'])):
        print(str(response['categories'][category]['categories']['id'])
              + ' ' + response['categories'][category]['categories']['name'])

        db_cur.execute("insert into ZMT_CATEGORIES values (:category_id, :category_name, SYSDATE)",
                       category_id=response['categories'][category]['categories']['id'],
                       category_name=response['categories'][category]['categories']['name'])

    db_conn.commit()


def get_cities(headers, query):
    response = requests.get(base_url + '/cities?q=' + query + '&count=1', params='', headers=headers).json()

    print(str(response['location_suggestions'][0]['country_id'])
          + ' ' + str(response['location_suggestions'][0]['country_name'])
          + ' ' + str(response['location_suggestions'][0]['id'])
          + ' ' + response['location_suggestions'][0]['name'])

    db_cur.execute("delete from ZMT_CITIES where CITY_ID = :city_id",
                   city_id=response['location_suggestions'][0]['id'])
    db_cur.execute("insert into ZMT_CITIES values (:city_id, :city_name, :country_id, :country_name, SYSDATE)",
                   city_id=response['location_suggestions'][0]['id'],
                   city_name=response['location_suggestions'][0]['name'],
                   country_id=response['location_suggestions'][0]['country_id'],
                   country_name=response['location_suggestions'][0]['country_name'])
    db_conn.commit()
    return str(response['location_suggestions'][0]['id'])


def get_collections(headers, city_id):
    response = requests.get(base_url + '/collections?city_id=' + city_id, params='', headers=headers).json()

    db_cur.execute("truncate table ZMT_COLLECTIONS")

    for collection in range(len(response['collections'])):
        print(str(response['collections'][collection]['collection']['collection_id'])
              + ' ' + str(response['collections'][collection]['collection']['res_count'])
              + ' ' + response['collections'][collection]['collection']['title']
              + ' ' + response['collections'][collection]['collection']['description']
              + ' ' + response['collections'][collection]['collection']['url']
              + ' ' + response['collections'][collection]['collection']['share_url'])
        db_cur.execute("insert into ZMT_COLLECTIONS values (:city_id, :collection_id, :title, :description, :url, "
                       ":share_url, :res_count, SYSDATE)",
                       city_id=city_id,
                       collection_id=response['collections'][collection]['collection']['collection_id'],
                       title=response['collections'][collection]['collection']['title'],
                       description=response['collections'][collection]['collection']['description'],
                       url=response['collections'][collection]['collection']['url'],
                       share_url=response['collections'][collection]['collection']['share_url'],
                       res_count=response['collections'][collection]['collection']['res_count'])

    db_conn.commit()
    return 0


def get_cuisines(headers, city_id):
    response = requests.get(base_url + '/cuisines?city_id=' + city_id, params='', headers=headers).json()

    db_cur.execute("truncate table ZMT_CUISINES")

    for cuisine in range(len(response['cuisines'])):
        print(str(response['cuisines'][cuisine]['cuisine']['cuisine_id'])
              + ' ' + response['cuisines'][cuisine]['cuisine']['cuisine_name'])
        db_cur.execute("insert into ZMT_CUISINES values (:city_id, :cuisine_id, :cuisine_name, SYSDATE)",
                       city_id=city_id,
                       cuisine_id=response['cuisines'][cuisine]['cuisine']['cuisine_id'],
                       cuisine_name=response['cuisines'][cuisine]['cuisine']['cuisine_name'])

    db_conn.commit()
    return 0


def get_establishments(headers, city_id):
    response = requests.get(base_url + '/establishments?city_id=' + city_id, params='', headers=headers).json()

    db_cur.execute("truncate table ZMT_ESTABLISHMENTS")

    for establishment in range(len(response['establishments'])):
        print(str(response['establishments'][establishment]['establishment']['id'])
              + ' ' + response['establishments'][establishment]['establishment']['name'])
        db_cur.execute("insert into ZMT_ESTABLISHMENTS values (:city_id, :establishment_id, :establishment_name, "
                       "SYSDATE)",
                       city_id=city_id,
                       establishment_id=response['establishments'][establishment]['establishment']['id'],
                       establishment_name=response['establishments'][establishment]['establishment']['name'])

    db_conn.commit()
    return 0


def get_locations(headers, query):
    response = requests.get(base_url + '/locations?query=' + query + '&count=1', params='', headers=headers).json()

    db_cur.execute("truncate table ZMT_LOCATIONS")

    print(str(response['location_suggestions'][0]['entity_id'])
          + ' ' + response['location_suggestions'][0]['entity_type']
          + ' ' + response['location_suggestions'][0]['title']
          + ' ' + str(response['location_suggestions'][0]['latitude'])
          + ' ' + str(response['location_suggestions'][0]['longitude'])
          + ' ' + str(response['location_suggestions'][0]['city_id'])
          + ' ' + response['location_suggestions'][0]['city_name']
          + ' ' + str(response['location_suggestions'][0]['country_id'])
          + ' ' + response['location_suggestions'][0]['country_name'])

    db_cur.execute("insert into ZMT_LOCATIONS values (:entity_id, :entity_type, :title, :latitude, :longitude, "
                   ":city_id, :city_name, :country_id, :country_name, SYSDATE)",
                   entity_id=response['location_suggestions'][0]['entity_id'],
                   entity_type=response['location_suggestions'][0]['entity_type'],
                   title=response['location_suggestions'][0]['title'],
                   latitude=response['location_suggestions'][0]['latitude'],
                   longitude=response['location_suggestions'][0]['longitude'],
                   city_id=response['location_suggestions'][0]['city_id'],
                   city_name=response['location_suggestions'][0]['city_name'],
                   country_id=response['location_suggestions'][0]['country_id'],
                   country_name=response['location_suggestions'][0]['country_name'])
    db_conn.commit()

    return str(response['location_suggestions'][0]['entity_id']), response['location_suggestions'][0]['entity_type']


def get_location_details(headers, entity_id, entity_type):
    response = requests.get(base_url + '/location_details?entity_id=' + entity_id + '&entity_type=' + entity_type,
                            params='', headers=headers).json()

    print(str(response['location']['entity_id'])
          + ' ' + response['location']['entity_type']
          + ' ' + str(response['popularity'])
          + ' ' + str(response['nightlife_index'])
          + ' ' + str(response['top_cuisines'])
          + ' ' + str(response['popularity_res'])
          + ' ' + str(response['nightlife_res'])
          + ' ' + str(response['num_restaurant']))

    db_cur.execute("delete from ZMT_LOCATIONS_EXT where ENTITY_ID = :entity_id", entity_id=entity_id)
    db_cur.execute("insert into ZMT_LOCATIONS_EXT values (TO_CHAR(SYSDATE, 'YYYYMM'), :entity_id, :popularity, "
                   ":nightlife_index, :top_cuisines, :popularity_res, :nightlife_res, :num_restaurant, SYSDATE)",
                   entity_id=entity_id,
                   popularity=response['popularity'],
                   nightlife_index=response['nightlife_index'],
                   top_cuisines=str(response['top_cuisines']),
                   popularity_res=response['popularity_res'],
                   nightlife_res=response['nightlife_res'],
                   num_restaurant=response['num_restaurant'])
    db_conn.commit()
    return 0


def get_search(headers, query, entity_id, entity_type):
    response = requests.get(base_url + '/search?entity_id=' + entity_id + '&entity_type=' + entity_type + '&q=' + query
                            + '&sort=rating&order=desc', params='', headers=headers).json()

    #print(response)
    #results_found = response['results_found']
    #results_start = response['results_start']
    #results_shown = response['results_shown']

    db_cur.execute("truncate table ZMT_RESTAURANTS")
    db_cur.execute("truncate table ZMT_RESTAURANTS_EXT")

    for restaurant in range(len(response['restaurants'])):
        print(str(response['restaurants'][restaurant]['restaurant']['id'])
              + ' ' + response['restaurants'][restaurant]['restaurant']['name']
              + ' ' + response['restaurants'][restaurant]['restaurant']['url']
              + ' ' + response['restaurants'][restaurant]['restaurant']['location']['locality']
              + ' ' + str(response['restaurants'][restaurant]['restaurant']['location']['city_id'])
              + ' ' + str(response['restaurants'][restaurant]['restaurant']['location']['latitude'])
              + ' ' + str(response['restaurants'][restaurant]['restaurant']['location']['longitude'])
              + ' ' + response['restaurants'][restaurant]['restaurant']['cuisines']
              + ' ' + str(response['restaurants'][restaurant]['restaurant']['average_cost_for_two'])
              + ' ' + str(response['restaurants'][restaurant]['restaurant']['user_rating']['aggregate_rating'])
              + ' ' + response['restaurants'][restaurant]['restaurant']['user_rating']['rating_text']
              + ' ' + str(response['restaurants'][restaurant]['restaurant']['user_rating']['votes'])
              + ' ' + str(response['restaurants'][restaurant]['restaurant']['has_online_delivery'])
              + ' ' + str(response['restaurants'][restaurant]['restaurant']['has_table_booking']))
        db_cur.execute("insert into ZMT_RESTAURANTS values (:restaurant_id, :restaurant_name, :url, :locality, "
                       ":city_id, :latitude, :longitude, SYSDATE)",
                       restaurant_id=response['restaurants'][restaurant]['restaurant']['id'],
                       restaurant_name=response['restaurants'][restaurant]['restaurant']['name'],
                       url=response['restaurants'][restaurant]['restaurant']['url'],
                       locality=response['restaurants'][restaurant]['restaurant']['location']['locality'],
                       city_id=response['restaurants'][restaurant]['restaurant']['location']['city_id'],
                       latitude=response['restaurants'][restaurant]['restaurant']['location']['latitude'],
                       longitude=response['restaurants'][restaurant]['restaurant']['location']['longitude'])
        db_cur.execute("insert into ZMT_RESTAURANTS_EXT values (TO_CHAR(SYSDATE, 'YYYYMM'), :restaurant_id, :cuisines, "
                       ":average_cost_for_two, :user_rating_aggregate, :user_rating_text, :user_rating_votes, "
                       ":has_online_delivery, :has_table_booking, SYSDATE)",
                       restaurant_id=response['restaurants'][restaurant]['restaurant']['id'],
                       cuisines=response['restaurants'][restaurant]['restaurant']['cuisines'],
                       average_cost_for_two=response['restaurants'][restaurant]['restaurant']['average_cost_for_two'],
                       user_rating_aggregate=response['restaurants'][restaurant]['restaurant']['user_rating']['aggregate_rating'],
                       user_rating_text=response['restaurants'][restaurant]['restaurant']['user_rating']['rating_text'],
                       user_rating_votes=response['restaurants'][restaurant]['restaurant']['user_rating']['votes'],
                       has_online_delivery=response['restaurants'][restaurant]['restaurant']['has_online_delivery'],
                       has_table_booking=response['restaurants'][restaurant]['restaurant']['has_table_booking'])
    db_conn.commit()
    return 0


def get_restaurant(headers, res_id):
    response = requests.get(base_url + '/restaurant?res_id=' + res_id, params='', headers=headers).json()

    print(str(response['id'])
          + ' ' + response['name']
          + ' ' + response['url']
          + ' ' + response['location']['locality']
          + ' ' + str(response['location']['city_id'])
          + ' ' + str(response['location']['latitude'])
          + ' ' + str(response['location']['longitude'])
          + ' ' + response['cuisines']
          + ' ' + str(response['average_cost_for_two'])
          + ' ' + str(response['user_rating']['aggregate_rating'])
          + ' ' + response['user_rating']['rating_text']
          + ' ' + str(response['user_rating']['votes'])
          + ' ' + str(response['has_online_delivery'])
          + ' ' + str(response['has_table_booking']))
    return 0


def main():
    headers = {'Accept': 'application/json', 'user-key': get_user_key()}
    city = 'Bangalore'
    locality = 'Sarjapur Road'

    #get_categories(headers)
    city_id = get_cities(headers, city)
    #get_collections(headers, city_id)
    #get_cuisines(headers, city_id)
    #get_establishments(headers, city_id)
    entity = get_locations(headers, locality)
    get_location_details(headers, entity[0], entity[1])
    #get_search(headers, locality, entity[0], entity[1])
    #get_restaurant(headers, '58882')


if __name__ == '__main__':
    main()
