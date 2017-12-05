from TwitterAPI import TwitterAPI
import json

# Open KEY files
with open('c:\\DEV\\GitHub\\python\\3.x\\keys\\twitter.key') as key_file_twitter:
    key_twitter = json.load(key_file_twitter)

api = TwitterAPI(key_twitter[0]['CONSUMER_KEY'],
                 key_twitter[0]['CONSUMER_SECRET'],
                 key_twitter[0]['ACCESS_TOKEN_KEY'],
                 key_twitter[0]['ACCESS_TOKEN_SECRET'])

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
