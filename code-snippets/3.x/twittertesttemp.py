# 05 Oct 2017 | Twitter Template using NXAuth

from nxauth import NXAuth

api = NXAuth().auth_twitter()

SEARCH_TERM = 'Sindhu'

r = api.request('search/tweets', {'q': SEARCH_TERM})
#for item in r:
    #print(item)
    #print(item['location'] if 'location' in item else item)

#r = api.request('statuses/filter', {'locations': '-74,40,-73,41'}) #New York
#r = api.request('statuses/filter', {'locations': '77, 12, 78, 13'}) #Bangalore
r = api.request('statuses/filter', {'locations': '37, 8, 97, 68'}) #India

for item in r:
    print(item)
    #print(item['location'] if 'location' in item else item)
