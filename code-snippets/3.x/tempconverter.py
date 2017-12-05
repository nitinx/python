# 14 Sep 2017 | Temperature Converter - Web Service, XML Parser, SQLite

import requests
import xml.etree.ElementTree as ET
import sqlite3
from contextlib import closing

rec = {}
str_in = input('From [(C)elsius / (F)ahrenheit]: ')
rec['fromv'] = input('Value: ')

if str_in == 'C':
    rec['from'] = 'Celsius'
    rec['to'] = 'Fahrenheit'
else:
    rec['from'] = 'Fahrenheit'
    rec['to'] = 'Celsius'

headers = {'content-type': 'application/soap+xml'}

url = "http://www.webservicex.net/ConvertTemperature.asmx?WSDL"

xmlreq = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <ConvertTemp xmlns="http://www.webserviceX.NET/">
      <Temperature>""" + rec['fromv'] + """</Temperature>
      <FromUnit>degree""" + rec['from'] + """</FromUnit>
      <ToUnit>degree""" + rec['to'] + """</ToUnit>
    </ConvertTemp>
  </soap12:Body>
</soap12:Envelope>"""

response = requests.post(url, data=xmlreq, headers=headers)
xmlres = str(response.content)[2:-1]
print(xmlres)

tree = ET.fromstring(xmlres)

# Output Format: Delimited
rec['tov'] = tree.find('.//{http://www.webserviceX.NET/}ConvertTempResult').text

print('"' + rec['from'] + '","' + rec['fromv'] + '","' + rec['to'] + '","' + rec['tov'] + '"')

create_sql = '''
create table tempconv (
    F TEXT,
    FValue NUMBER,
    T TEXT,
    TValue NUMBER
)'''

insert_sql = '''insert into tempconv (F, FValue, T, TValue) values (?, ?, ?, ?)'''

select_sql = '''select F, FValue, T, TValue from tempconv'''

with closing(sqlite3.connect('tempconv.sqlite')) as con:
    #con.execute(create_sql)
    con.execute(insert_sql, (rec['from'], rec['fromv'], rec['to'], rec['tov']))
    con.commit()
    con.close()

with closing(sqlite3.connect('tempconv.sqlite')) as con:
        for row in con.execute(select_sql):
            print(row)
