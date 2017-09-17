from TwitterAPI import TwitterAPI
import cx_Oracle

# Twitter Credentials
CONSUMER_KEY = 'Vn6dl2pDjDHsn9sELnNztv44K'
CONSUMER_SECRET = 'TKsAzjqhtsTDERmAMZZRFzT6YlVfmb4aYc6Dj9FJGpF3aInHbP'
ACCESS_TOKEN_KEY = '18508737-OehQWEqOWjqac21ochmM908YGiydBHe4E1HF0unZ1'
ACCESS_TOKEN_SECRET = 'EsUfX8hbPsDeMQhJbrRY1wlW1rjI2tlqik9qTfFTxflAi'

# Oracle Connection Values
USER = "infa"
PASSWORD = "pass"
CONNECT_STRING = "localhost"

connection = cx_Oracle.connect(USER, PASSWORD, CONNECT_STRING)
cursor = connection.cursor()

api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
SEARCH_TERM = 'Dhoni'

r = api.request('search/tweets', {'q': SEARCH_TERM})

for item in r:
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
                   user_name=ascii(item['user']['name']),
                   #user_screen_name=str.encode(item['user']['screen_name'], encoding='ascii', errors='ignore'),
                   user_screen_name=ascii(item['user']['screen_name']),
                   #user_created_at=(item['user']['created_at'][-4:] + item['user']['created_at'][-3:19]),
                   #text=str.encode(item['text'], encoding='ascii', errors='ignore')
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