# 29 Mar 2017 | SOAP Request / Response

import requests

'''
Best practise would be to store request as a template, then load it using jinja2 (for example) - and also pass in variables.
from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('myapp', 'templates'))
template = env.get_template('soaprequests/WeatherSericeRequest.xml')
body = template.render()
'''

#headers = {'content-type': 'application/soap+xml'}
headers = {'content-type': 'text/xml'}

url1 = "http://wsf.cdyne.com/WeatherWS/Weather.asmx?WSDL"

body1 = """<?xml version="1.0" encoding="UTF-8"?>
         <SOAP-ENV:Envelope xmlns:ns0="http://ws.cdyne.com/WeatherWS/" xmlns:ns1="http://schemas.xmlsoap.org/soap/envelope/"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
            <SOAP-ENV:Header/>
              <ns1:Body><ns0:GetWeatherInformation/></ns1:Body>
         </SOAP-ENV:Envelope>"""

url = "http://www.webservicex.net/ConvertTemperature.asmx?WSDL"
body = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <ConvertTemp xmlns="http://www.webserviceX.NET/">
      <Temperature>50</Temperature>
      <FromUnit>degreeCelsius</FromUnit>
      <ToUnit>degreeFahrenheit</ToUnit>
    </ConvertTemp>
  </soap12:Body>
</soap12:Envelope>"""

response = requests.post(url, data=body, headers=headers)

print(response.content)
