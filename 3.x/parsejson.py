# 22 Mar 2017 | Parser - JSON

import json
from pprint import pprint

with open('sample_nested.json') as data_file:
    data = json.load(data_file)

print('# of records:', len(data))

# Output Format: Delimited
for row_main in range(len(data)):
    print('"' + data[row_main]['id'] + '","'
          + data[row_main]['type'] + '","'
          + data[row_main]['name'] + '","'
          + str(data[row_main]['ppu']) + '"' )

    # print(len(data[row]['batters']['batter']))

    for row_batter in range(len(data[row_main]['batters']['batter'])):
        print('\t"' + data[row_main]['id'] + '","'
              + data[row_main]['batters']['batter'][row_batter]['id'] + '","'
              + data[row_main]['batters']['batter'][row_batter]['type'] + '"')

    for row_topping in range(len(data[row_main]['topping'])):
        print('\t\t"' + data[row_main]['id'] + '","'
              + data[row_main]['topping'][row_topping]['id'] + '","'
              + data[row_main]['topping'][row_topping]['type'] + '"')

# pprint(data)
