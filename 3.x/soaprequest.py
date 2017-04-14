# 29 Mar 2017 | SOAP Request / Response

import requests

'''
Best practise would be to store request as a template, then load it using jinja2 (for example) - and also pass in variables.
from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('myapp', 'templates'))
template = env.get_template('soaprequests/WeatherSericeRequest.xml')
body = template.render()
'''

url = "http://wsf.cdyne.com/WeatherWS/Weather.asmx?WSDL"

#headers = {'content-type': 'application/soap+xml'}
headers = {'content-type': 'text/xml'}

body = """<?xml version="1.0" encoding="UTF-8"?>
         <SOAP-ENV:Envelope xmlns:ns0="http://ws.cdyne.com/WeatherWS/" xmlns:ns1="http://schemas.xmlsoap.org/soap/envelope/"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
            <SOAP-ENV:Header/>
              <ns1:Body><ns0:GetWeatherInformation/></ns1:Body>
         </SOAP-ENV:Envelope>"""

response = requests.post(url, data=body, headers=headers)

print(response.content)
