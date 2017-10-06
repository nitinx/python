# 05 Oct 2017 | App Authenticator

from TwitterAPI import TwitterAPI
import json

class NXAuth:

    def auth_twitter(self):
        # Open KEY files
        with open('c:\\DEV\\GitHub\\python\\3.x\\keys\\twitter.key') as key_file_twitter:
            key_twitter = json.load(key_file_twitter)

        api = TwitterAPI(key_twitter[0]['CONSUMER_KEY'],
                         key_twitter[0]['CONSUMER_SECRET'],
                         key_twitter[0]['ACCESS_TOKEN_KEY'],
                         key_twitter[0]['ACCESS_TOKEN_SECRET'])
        return api


    def auth_instagram(self):
        # Open KEY files
        with open('c:\\DEV\\GitHub\\python\\3.x\\keys\\instagram.key') as key_file_instagram:
            key_instagram = json.load(key_file_instagram)

        api = InstagramAPI(key_instagram[0]['CONSUMER_KEY'],
                           key_instagram[0]['CONSUMER_SECRET'],
                           key_instagram[0]['ACCESS_TOKEN_KEY'],
                           key_instagram[0]['ACCESS_TOKEN_SECRET'])
        return api


    def auth_facebook(self):
        # Open KEY files
        with open('c:\\DEV\\GitHub\\python\\3.x\\keys\\facebook.key') as key_file_facebook:
            key_facebook = json.load(key_file_facebook)

        api = FacebookAPI(key_facebook[0]['CONSUMER_KEY'],
                          key_facebook[0]['CONSUMER_SECRET'],
                          key_facebook[0]['ACCESS_TOKEN_KEY'],
                          key_facebook[0]['ACCESS_TOKEN_SECRET'])
        return api
