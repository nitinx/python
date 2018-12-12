from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json


# Load Credentials
with open('e:\\GitHub\\python\\keys\\twitter.key', 'r') as key_file_twitter:
    key_twitter = json.load(key_file_twitter)

consumer_key = key_twitter[0]['CONSUMER_KEY']
consumer_secret = key_twitter[0]['CONSUMER_SECRET']
access_token = key_twitter[0]['ACCESS_TOKEN_KEY']
access_token_secret = key_twitter[0]['ACCESS_TOKEN_SECRET']

# Instantiate an object


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        js = json.loads(data)
        print(js)
        print(js['text'])
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['basketball'])
