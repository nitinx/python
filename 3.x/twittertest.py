from TwitterAPI import TwitterAPI

CONSUMER_KEY = 'Vn6dl2pDjDHsn9sELnNztv44K'
CONSUMER_SECRET = 'TKsAzjqhtsTDERmAMZZRFzT6YlVfmb4aYc6Dj9FJGpF3aInHbP'
ACCESS_TOKEN_KEY = '18508737-OehQWEqOWjqac21ochmM908YGiydBHe4E1HF0unZ1'
ACCESS_TOKEN_SECRET = 'EsUfX8hbPsDeMQhJbrRY1wlW1rjI2tlqik9qTfFTxflAi'

api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

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
