# 23 Sep 2017 | Twitter Client/Integration

from TwitterAPI import TwitterAPI
import cx_Oracle
import sys
import json

# Open KEY files
with open('c:\\DEV\\GitHub\\python\\keys\\twitter.key') as key_file_twitter:
    key_twitter = json.load(key_file_twitter)

with open('c:\\DEV\\GitHub\\python\\keys\\oracle.key') as key_file_oracle:
    key_oracle = json.load(key_file_oracle)

connection = cx_Oracle.connect(key_oracle[0]['USER'],
                               key_oracle[0]['PASSWORD'],
                               key_oracle[0]['CONNECT_STRING'])
cursor = connection.cursor()

api = TwitterAPI(key_twitter[0]['CONSUMER_KEY'],
                 key_twitter[0]['CONSUMER_SECRET'],
                 key_twitter[0]['ACCESS_TOKEN_KEY'],
                 key_twitter[0]['ACCESS_TOKEN_SECRET'])
SEARCH_TERM = 'Dhoni'

r = api.request('search/tweets', {'q': SEARCH_TERM})

for item in r:
    print(sys.stdout.encoding)
    print(item['id'],
          item['created_at'][-4:] + item['created_at'][3:19],
          item['user']['id'],
          item['user']['name'],
          item['user']['screen_name'],
          item['user']['created_at'][-4:] + item['user']['created_at'][-3:19],
          item['text'])

    cursor.execute("INSERT INTO twitter_tweets values (:id, "
                                                       "TO_TIMESTAMP(:time, 'YYYY Mon DD HH24:MI:SS'), "
                                                       ":user_id, "
                                                       "SUBSTR(:user_name, 1, 50), "
                                                       "SUBSTR(:user_screen_name, 1, 50), "
                                                       "NULL, "
                                                       "SUBSTR(:text, 1, 150))",
                   id=item['id'],
                   time=(item['created_at'][-4:] + item['created_at'][3:19]),
                   user_id=item['user']['id'],
                   #user_name=str.encode(item['user']['name'], encoding='ascii', errors='ignore'),
                   #user_name=ascii(item['user']['name']),
                   user_name=ascii(item['user']['name']),
                   #user_screen_name=str.encode(item['user']['screen_name'], encoding='ascii', errors='ignore'),
                   user_screen_name=ascii(item['user']['screen_name']),
                   #user_created_at=(item['user']['created_at'][-4:] + item['user']['created_at'][-3:19]),
                   #text=str.encode(item['text'], encoding='utf-8', errors='replace')
                   #text=item['text'].encode(sys.stdout.encoding, errors='replace')
                   text=ascii(item['text'])
                   )
    connection.commit()

'''
cursor.execute("""
	    SELECT id, time, user_name, text
	    FROM twitter_tweets""")

for id, time, user_name, text in cursor:
    print("Values:", id, time, user_name, text)
'''
