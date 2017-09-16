# 14 Sep 2017 | Public APIs, JSON Parser

import requests
import json
from pprint import pprint
import urllib

url = "https://restcountries.eu/rest/v2/name/France?fullText=true"
data = json.load(urllib.request.urlopen(url))

print(data)

print('# of records:', len(data))

# Output Format: Delimited
for row_main in range(len(data)):
    print('"' + str(data[row_main]['name']) + '","'
          + str(data[row_main]['topLevelDomain']) + '","'
          + str(data[row_main]['alpha2Code']) + '","'
          + str(data[row_main]['alpha3Code']) + '","'
          + str(data[row_main]['callingCodes']) + '","'
          + str(data[row_main]['capital']) + '","'
          + str(data[row_main]['region']) + '","'
          + str(data[row_main]['population']) + '","'
          + str(data[row_main]['latlng']) + '","'
          + str(data[row_main]['timezones']) + '","'
          + str(data[row_main]['borders']) + '","'
          + str(data[row_main]['nativeName']) + '"'
          )

'''    for row_batter in range(len(data[row_main]['batters']['batter'])):
        print('\t"' + data[row_main]['id'] + '","'
              + data[row_main]['batters']['batter'][row_batter]['id'] + '","'
              + data[row_main]['batters']['batter'][row_batter]['type'] + '"')

    for row_topping in range(len(data[row_main]['topping'])):
        print('\t\t"' + data[row_main]['id'] + '","'
              + data[row_main]['topping'][row_topping]['id'] + '","'
              + data[row_main]['topping'][row_topping]['type'] + '"')
'''